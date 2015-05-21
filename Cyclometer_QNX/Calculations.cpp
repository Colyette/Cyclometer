 /**
 * @file: Calculations.cpp
 * @brief: Performs the calculations required for display on the Cyclometer
 * @author: Alyssa Colyette
 */
#include "Calculations.h"

#define WHEEL_TIME_OUT ( 850000000) // .85s

#define TEST_CALCULATIONS 1

//constructor
Calculations::Calculations(){
	_speed = _avg =_dist=0;

#ifdef TEST_CALCULATIONS
	//Testin Auto calculations at default wheel size
	//WheelRot=1;
	tireSize = 210;
	cetime =100;
	Auto =1;
	TCalcFlg=0;
#endif
}

//destructor
Calculations::~Calculations(){

}


//state machine is not really trigger event based, only outside event is poRest
int Calculations::runCalculationsStateMachine(){
	int pCnt=0;
	struct _pulse pulse; //for timer msg
 	int chid,pid; //for target of timer msg passing
	int _run =1;
    chid= _InitializeAccumTimer(WHEEL_TIME_OUT,5); //returns the ch id for send messages
	while (_run) {
		switch (curState) {
			case ACCUM_WAIT: 
				//wait for tm
				pid = MsgReceivePulse(chid,&pulse,  sizeof( pulse ),NULL);
				//::sleep(1);
				curState =DET_MOTION;
			case DET_MOTION: //want to fall here anyway
				//read pulse counter
				pCnt = pc->getCount();
				printf("pCnt:%d\n",pCnt);
				//clear pulse counter
				pc->clearCount();
				if (pCnt) { //there is motion
					curState = SPEED_UPDATE;
					//TODO trigger actions
					//toggleLED(WHEEL_LED)
					//WheelRot =1;
				} else { //too slow for detection, no motion
					curState = DET_TRIP_CALC;
					//TODO trigger actions
					//TODO maybe a call to display,turnOff(WHEEL_LED);
					//WheelRot =0;
				} //end of transition from DET_MOTION
				break;

			case SPEED_UPDATE:
				//calc speed
				calcSpeed(pCnt); //TODO use universal speed variable?
				if (Auto) { //cal trips
					curState = TRIP_CALC_UPDATE;
				} else{ //determine if manual mode start
					if(TCalcFlg) { //calc trips
						curState = TRIP_CALC_UPDATE;
					}else { //don't calc trips
						curState = ACCUM_WAIT;
						throwEvent(calcUpdate);
					}
				}
				break;

			case DET_TRIP_CALC:
				if (Auto) { //no motion so no trip calc
					curState = ACCUM_WAIT;
					throwEvent(calcUpdate);

				} else { // manual mode
					if(TCalcFlg) { //still perform calc in manual
						curState = TRIP_CALC_UPDATE;
					} else { // man calc turned off
						curState = ACCUM_WAIT;
						throwEvent(calcUpdate);
					}
				}
				break;

			case TRIP_CALC_UPDATE:
				calcDistance(pCnt);
				calcAvgSpeed();
				curState = ACCUM_WAIT;
				throwEvent(calcUpdate);
				break;

			case PO_RESET_CALC:
				//restart system?
				curState = ACCUM_WAIT;//??
				_run = 0;
				break;
			default:
				//error, just go back to wait state
				curState = ACCUM_WAIT;
				break;
		} //end switch curState
	} //end while
	return 1;
}

/**
 * @brief Does the current speed calculation from the latest pulse count collected
 */
int Calculations::calcSpeed(int pulseCount){
	//TODO need wheel size
	_speed = pulseCount/(WHEEL_TIME_OUT/1000000000.0 );
	_speed = _speed * (tireSize/100000.0)*(3600.0);  //kph
#ifdef TEST_CALCULATIONS
	printf("cs:%f\n",_speed);
#endif
	return 1; //TODO may need to return speed and type double 
}

/**
 * @brief Calculates and accumulates the total distance traveled
 */
int Calculations::calcDistance(int pulseCount){
	_dist += pulseCount*(tireSize*pow(10,-5) ); //km
#ifdef TEST_CALCULATIONS
	printf("d:%f\n",_dist);
#endif
	return 1; 
}

/**
 * @brief Does the average speed calculations
 * @precon calcDistance called beforehand for correct distance update
 */
int Calculations::calcAvgSpeed(){
	//TODO need elapse time
	_avg = _dist/cetime;
#ifdef TEST_CALCULATIONS
	printf("avg:%f\n",_avg);
#endif
	return 1;
}

int Calculations::throwEvent(events e){
	//TODO
	return 1;
}

//timer for waiting until the next pulse is received
int Calculations::_InitializeAccumTimer(long nsfreq, int pulseid){
	  int chid;
	  timer_t timer_id;
	  struct sigevent event;
	  struct itimerspec timer;
	  printf("Initializing Pulses at %ldns with pulse id as %d\n", nsfreq, pulseid);

	  /* Create a channel to receive timer events on. */
	  chid = ChannelCreate( 0 ); //b: opening up a channel to send messages through
	  assert ( chid != -1 );      // if returns a -1 for failure we stop with error
	  /* Set up the timer and timer event. */
	  event.sigev_notify = SIGEV_PULSE;   // most basic message we can send -- just a pulse number
	  event.sigev_coid = ConnectAttach ( ND_LOCAL_NODE, 0, chid, 0, 0 );  // Get ID that allows me to communicate on the channel
	  assert ( event.sigev_coid != -1 );    // stop with error if cannot attach to channel
	  event.sigev_priority = getprio(0);
	  event.sigev_value.sival_int = pulseid;

	  // Now create the timer and get back the timer_id value for the timer we created.
	  if ( timer_create( CLOCK_REALTIME, &event, &timer_id ) == -1 )  // CLOCK_REALTIME available in all POSIX systems
	  {
		perror ( "cannot create timer\n" );
		exit( EXIT_FAILURE );
	  }

	  /* Change the timer request to alter the behavior. */
	  timer.it_value.tv_sec = 0;
	  timer.it_value.tv_nsec = nsfreq;    // interrupt nsfreq -> period
	  timer.it_interval.tv_sec = 0;
	  timer.it_interval.tv_nsec = nsfreq; // keep interrupting nsfreq

	  /* Start the timer. */
	  if ( timer_settime( timer_id, 0, &timer, NULL ) == -1 )
	  {
		perror("cannot start timer.\n");
		exit( EXIT_FAILURE );
	  }

	  return chid;
}

#ifdef TEST_CALCULATIONS
//should attach and run wheel sensor, while spamming speed, avg speed, and distance
int main () {
	Calculations cal = Calculations();
	WheelSensor ws = WheelSensor();
	cal.attachPulseCounter(&ws);
	pthread_t wThread;
	//TODO this should be spawned by calculations class?
	if (pthread_create (&wThread, NULL,startWheelSensor, &ws)) {
	        printf("WheelSensor MainThread: error running thread\n");
	        return -1;
	 }
	
	while (1) {
		cal.runCalculationsStateMachine();
	}
}
#endif //CALCULATIONS


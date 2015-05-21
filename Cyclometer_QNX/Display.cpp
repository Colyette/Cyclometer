/**
 * @file Display.cpp
 * @brief Controls 7-segment display of Cyclometer depending on internal state
 * and variable flgs
 * @author Alyssa Colyette
 */

#include "Display.h"
#include "WheelSensor.h"
#include "PulseCounter.h"
//
#include <pthread.h>

#define POLL_RATE (5000000)//(13) //frequency for 7 seg display ~50/4 Hz

#define ELAPSE_RES (999999999)	 //~1 second resolution can't do 1s invalid arg

#define TEST_DISPLAY 1 	//activates the main for display tests

void * DisplayRefreshHelper(void* instance) {
	Display* c_instance = (Display*) instance;
	printf("DisplayRefreshHelper: going into refresh thread\n");
	c_instance->refreshDisplay(); //casted to instantiated class and run main thread funct
	return 0 ;
}

void * DisplayElapseTimerHelper(void* instance) {
	Display* c_instance = (Display*) instance;
	printf("DisplayElapseTimerHelper: going into elapse timer thread\n");
	c_instance->runTimer(); //casted to instantiated class and run main thread funct
	return 0 ;
}

//contructor and destructor for display class
Display::Display(){
    curSuper = RESET;
    curSub = NUM_M_STATES;
    curSubr = INIT_DATA;
    //init stuff
    d_i_o_control_handle = -1;     // control register for ports A, B, and C
    d_i_o_port_a_handle = -1;
    d_i_o_port_b_handle = -1;

    _run = 1;

#ifdef TEST_DISPLAY
    printf("Testing with feed values for speed,avg,dist,time,unit,tiresize\n");
    //for testing the display format without implementing the state machine
    curSuper = MAIN;
    curSub = ELAPSE_DISPLAY;
    curSubr = NUM_R_STATES;
//    curSuper = RESET;
//       curSub = NUM_M_STATES;
//       curSubr = SET_TIRE_SIZE;

    //values
    cspeed= 7;
    cavg = 5;
    cdistance =0.2 ;
    cetime= 0;     //in seconds ~16:40
    unit=0;       //flg like 0 or 1
    tireSize=210;
#endif
}

Display::~Display(){
    _run = 0;
    //join threads..
}

/**
 * @brief Runs the elapse timer if trip calculations are on, the elapse
 * time is updated
 */
int Display::runTimer(){
	struct _pulse pulse; //for timer msg
    int chid,pid; //for target of timer msg passing 
    chid= _InitializeSegmentTimer(ELAPSE_RES,2); //returns the ch id for send messages
//TODO may have to look into pulse ID other than 1
	while(_run) {
		pid = MsgReceivePulse(chid,&pulse,  sizeof( pulse ),NULL);
		if (AUTO && (true)) { // TODO Auto mode, and motion is detected (REPLACE 'TRUE')
			cetime++;
		}
		else if (0) { //TODO Manual Mode and calc is on
			cetime++;
		}
	}
	return 1;
}

/**
 * @brief Gets route access for the requesting thread
 */
int Display::_GetRootAccess(){
    int status = 0 ;
    int privity_err ;

    /* Give this thread root permissions to access the hardware */
    privity_err = ThreadCtl( _NTO_TCTL_IO, NULL );
    if ( privity_err == -1 )
    {
        fprintf( stderr, "can't get root permissions\n" );
        status = -1;
    }
    return status ;
}



/**
 * \brief Sets the port direction to output
 */
int Display::_setPortDirection(){
        out8( d_i_o_control_handle, DIO_DIR) ;     // make port A input,B output
        printf("Set A as input and B as output\n");
        return 1;
}

/**
 * @brief inits the DIO on the data ack port
 */
int Display::initDIO(){
	if ( !_GetRootAccess()){
		d_i_o_control_handle = mmap_device_io( D_I_O_PORT_LENGTH, D_I_O_CONTROL_REGISTER ) ;
		d_i_o_port_a_handle = mmap_device_io( D_I_O_PORT_LENGTH, D_I_O_PORT_A ) ;
		d_i_o_port_b_handle = mmap_device_io( D_I_O_PORT_LENGTH, D_I_O_PORT_B ) ;
		_setPortDirection();
	}else {
	        printf("Couldn't get root access to set DIO ports\n");
	        return (-1);
	}
	return 1;
}


/**
 * @brief starts the statemachine for the display.
 * @precon: DIO is initialized
 */
int Display::run(){ //TODO maybe initialize DIO in run???
    //run refresh display thread
    if (pthread_create (&segmentRunner, NULL, DisplayRefreshHelper, this)) { 
        printf("Display MainThread: error creating dio Display processing thread\n");
        return -1;
    }
	//run elaspe timer
 	if (pthread_create (&eTimerThread, NULL, DisplayElapseTimerHelper, this)) { 
        printf("Display MainThread: error creating elapse timer thread\n");
        return-2;
    }
    //check for changing states
    while (1) {
    	// check for next event recognized
    	if (curEvent !=NUM_EVENTS) { //a new event was trigggered
    		// process the event
    		runDisplayStateMachine();
    	}
    }
	return 1;
}

/**
 * @brief for doing timeouts in a state where other triggers are possible
 * starts a timeout of the provided time, use timeout() to determine it 
 * timeout has passed.
 */
int Display::startTimeout(int time_ns){
	
    tmchid= _InitializeSegmentTimer(time_ns,3); //returns the ch id for send messages
	//TODO spawn a thread that sets a flg after pulse received?
	//TODO if so, have thread close itself safely after somehow...
    return 0;
}
 
/**
 * @brief pollable function to determine if a timeout has occured
 * @returns 0:no, 1:yes, 2:no timer was initialized yet
 */
int Display::timeout(){
	 //pid = MsgReceivePulse(chid,&pulse,  sizeof( pulse ),NULL);
	//TODO checks if a spawned thread enters its pulse received state?
	return 0;
}

/**
 * @brief for processing events in the reset state
 */
void Display::_resetState() {
	switch (curSubr) {
		case INIT_DATA:
			Init = 1;
			AUTO = 0; //manual
			TCalcFlg =0; //calc off
			unit = 0; //unit kph
			tireSize = 210; 
			//reset trip values
			cavg = 0;
			cdistance =0;
			cetime=0;
			curSubr = UNIT_SELECT;
			break;
    	case UNIT_SELECT:
			switch (curEvent) {
				case m_press:
					//TODO toggle Unit
					//TODO change LED
					break;
				case s_press:
					curSubr = SET_TIRE_SIZE;
					break;
				default:
					break;
			}
        	break;
    	case SET_TIRE_SIZE:
			switch (curEvent) {
				case m_press:
					tireSize++;
					if (tireSize < 220) {
						tireSize = 190;
					}
					break;
				case s_press:
					if (Init) {
						// maybe spawn timer in here instead.. or clr accum
						cetime = 0;
						//go to speed display
						curSuper = MAIN;
						curSubr = NUM_R_STATES;
						curSub =SPEED_DISPLAY;
					} else { //recently came from an re-prog tire size
						curSuper = MAIN;
						curSubr = NUM_R_STATES;
						curSub =DISTANCE_DISPLAY;
					}
				case m_hold:
					curSubr = M_HOLD_WAIT;
				default:
					break;
			}
        	break;
    	case M_HOLD_WAIT:
			switch (curEvent) {
				case m_release:
				//TODO TIMEOUT SOMEHOW...
				default:
					break;
			}
			break;
     	case TIRE_AUTO:
            switch (curEvent) {
				case m_release:
				//TODO TIMEOUT SOMEHOW...
				default:
					break;
			}           
        	break; //for preceding 3 states same display
       	default:
                	printf("not a valid reset state\n");
                	break; 
    }//end reset cases
	
}

/**
 * @brief for processing events in the reset state
 */
void Display::_mainState() {
	switch (curSub) { 
		case DISTANCE_DISPLAY:
			//all main states process the same events accept can change tire size
			switch (curEvent) {
				case m_press:
					curSub = ELAPSE_DISPLAY;
					break;
				case ss_press:
					if (!AUTO) { //if manual toggle TCalcFlg
						if (TCalcFlg) {
							TCalcFlg =0;
						} else {
							TCalcFlg =1;
						}
					}
					break;
				case tReset: //clear trip values
					cavg = 0;
					cdistance =0;
					cetime=0;
					break;
				case calcUpdate:
					//TODO force screen refresh, my not be needed, 
					// but values are external still..
					break;
				case s_press:
					//TODO got to tire settings
					curSuper = RESET;
					curSub = NUM_M_STATES;
					curSubr = SET_TIRE_SIZE;
					break;
				case poReset:
					curSuper = PO_RESET;
					curSub = NUM_M_STATES;
					curSubr = NUM_R_STATES;
					break;
				default:
					break;
			}
			break;
		case SPEED_DISPLAY:
			Init =0; //not in PO init anymore
    	case ELAPSE_DISPLAY:
			switch (curEvent) {
				case m_press:
					if (curSub == SPEED_DISPLAY) {
						curSub = DISTANCE_DISPLAY;
					} else {
						curSub = SPEED_DISPLAY;
					}
					
					break;
				case ss_press:
					if (!AUTO) { //if manual toggle TCalcFlg
						if (TCalcFlg) {
							TCalcFlg =0;
						} else {
							TCalcFlg =1;
						}
					}
					break;
				case tReset: //clear trip values
					cavg = 0;
					cdistance =0;
					cetime=0;
					break;
				case calcUpdate:
					//TODO force screen refresh, my not be needed, 
					// but values are external still..
					break;
				case s_press:
					//toggle user mode
					if (AUTO) {
						AUTO =0;
					} else {
						AUTO =1;
					} 
					//TODO throw user toggled

					break;
				case poReset:
					curSuper = PO_RESET;
					curSub = NUM_M_STATES;
					curSubr = NUM_R_STATES;
					break;
				default:
					break;
			}
			break;
       	default:
        	printf("not a valid reset state\n");
        	break; 
    }//end reset cases
	
}

/**
 * @brief  run display state machine, determines next state from state transistion
 */
int Display::runDisplayStateMachine () {
    //TODO
	switch(curSuper) {
		case RESET: 
			_resetState(); 
			
			break;
		case MAIN:
			_mainState();
			break;
		case PO_RESET:
			break;
		default:
			printf("Not a real superstate\n");
			break;
	}
	//rid handled event
	curEvent = NUM_EVENTS;
	return 1; //TODO say if event was handled?
}


// 7 Segment Display Code~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
int Display::_InitializeSegmentTimer(long nsfreq, int pulseid){
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

/**
 * @brief Converts the provided digit into its 8 bit 7 segment display value
 */
uint8_t Display::digitToSegment(int digit) {
    uint8_t converted;
    switch (digit) {
        case 0:
            converted = 0b00111111;
            break;
        case 1:
            converted = 0b00000110;
            break;
        case 2:
            converted = 0b01011011;
            break;
        case 3:
            converted = 0b01001111;
            break;
        case 4:
            converted = 0b01100110;
            break;
        case 5:
            converted = 0b01101101;
            break;
        case 6:
            converted = 0b01111101;
            break;
        case 7:
            converted = 0b00000111;
            break;
        case 8:
            converted = 0b01111111;
            break;
        case 9:
            converted = 0b01101111;
            break;
        default:
            printf("not a single digit value: %d\n", digit);
            converted = 0;
            break;
    }
    return converted;
}



//controls 7 seg display with internal variables and current state flgs
void Display::refreshDisplay(){
    uint8_t dis0,dis1,dis2,dis3; //l to r
    uint8_t pAwrite;
//TODO set up DIO
    //init Timer
    printf("Display::refreshDisplay(): Creating 7 seg display timer\n");
    struct _pulse pulse; //for timer msg
    int chid,pid; //for target of timer msg passing
    chid= _InitializeSegmentTimer(POLL_RATE,1); //returns the ch id for send messages
    printf("Entering with states Sup:%d Sur:%d Sum:%d\n", curSuper,curSubr, curSub);
    while (_run) {
        //check state to formate diplay correctly
        //use some flg set after calc update?
//#ifndef TEST_DISPLAY //logic doesn't really effect display timing
        switch (curSuper) {
            case RESET:
                switch (curSubr) {
                    case UNIT_SELECT:

                        _refreshUnitDisplay(&dis0,&dis1,&dis2,&dis3); //TODO test conversion
//                        dis0 = dis1 = dis2 =0; //blank the displays
//                        dis3 = digitToSegment (1); //TODO actual units variable

                        break;
                    case SET_TIRE_SIZE:
                    case M_HOLD_WAIT:
                    case TIRE_AUTO:
                        _refreshTireDisplay(&dis0, &dis1, &dis2, &dis3);  //TODO error check return and test conversion
//                        dis0 = 0; //blank left most display
//                        dis1 = digitToSegment(9);
//                        dis2 = digitToSegment(8);
//                        dis3 = digitToSegment(7); //TODO actual circumference with decimal masking
                    	break; //for preceding 3 states same display
                    default:
                        printf("not a valid reset state\n");
                        break;
                }//end reset cases
                break; //RESET SUBSTATE CASE

            case MAIN:
                switch (curSub) {
                    case SPEED_DISPLAY:
                        //TODO fix pulse counter for tenth decimal values as pre requirements
                      //TODO not going here for some reason printf(".");
                    	_refreshSpeedDisplay(&dis0, &dis1, &dis2, &dis3);  //TODO error check return
//                        dis0 = digitToSegment(9);
//                        dis1 = digitToSegment(8);
//                        dis2 = digitToSegment(7);
//                        dis3 = digitToSegment(8);
                        break;
                    case DISTANCE_DISPLAY:
                        _refreshDistDisplay(&dis0, &dis1, &dis2, &dis3);  //TODO error check return
//                        dis0 = digitToSegment(9); //(dec)
//                        dis1 = digitToSegment(8); //(dec)
//                        dis2 = digitToSegment(7); //(dec)
//                        dis3 = digitToSegment(6); //(dec)
//                        dis3 |=SDP;
                        break;
                    case ELAPSE_DISPLAY:
                        _refreshElapseDisplay(&dis0, &dis1, &dis2, &dis3);  //TODO error check return
//                        dis0 = digitToSegment(7); //(d1)
//                        dis1 = digitToSegment(7); //(d2)
//                        dis2 = digitToSegment(6); //(d1)
//                        dis3 = digitToSegment(6); //(d2)
                        break;

                    default:
                        printf("Not in a state with a display\n");
                        break;
                } //end main cases

                break;
            case PO_RESET:
                printf("not updating display due to reset state\n");
                break;
            default:
                printf("Not in a valid display state\n");
                break;
        }
//#endif //TEST_DISPLAY

//TODO might want to separate state/display determination for better display refresh w/o num change
//TODO switching order dist0 == an3
        //TODO segments and anodes are active low?
#ifdef TEST_DISPLAY_FEED
//        dis0=digitToSegment(1);
//        dis1= digitToSegment(2);
//        dis2=digitToSegment(5);
//        dis3=digitToSegment(9);
printf(".");
        dis0=dis1=dis2=dis3=0x00; //TESTING PORT B DIO
#endif //TEST_DISPLAY

        //display for each digit/anode
        //assign digit value for left most
        pAwrite = in8 (d_i_o_port_a_handle);
        //pAwrite = pAwrite & ~A1 & ~A2 & ~A3; //turn off all anodes but 0
        pAwrite = pAwrite | A1 | A2 | A3; //turn off all anodes but 0, w/ high sigs
        pAwrite &= ~A0; //clear A0
        out8(d_i_o_port_a_handle, pAwrite);
        out8(d_i_o_port_b_handle,(uint8_t)~dis3);// ~dis3);
        //printf("%x\n",(uint8_t)~dis3);
        //printf("%u\n",pAwrite);
        //sleep 
        pid = MsgReceivePulse(chid,&pulse,  sizeof( pulse ),NULL);

        //assign 2nd leftmost digit
        pAwrite = in8(d_i_o_port_a_handle);
        pAwrite = pAwrite | A0 | A2 |A3; //turn off all anodes but 1
        pAwrite &= ~A1;
        out8(d_i_o_port_a_handle, pAwrite);
        out8(d_i_o_port_b_handle,(uint8_t) ~dis2);
        //printf("%x\n",(uint8_t)~dis2);
        //sleep
        pid = MsgReceivePulse(chid,&pulse,  sizeof( pulse ),NULL);

        pAwrite = in8(d_i_o_port_a_handle);
        pAwrite = pAwrite |A0 |A1 |A3; //turn off all anodes but 1
        pAwrite &= ~A2;
        out8(d_i_o_port_a_handle, pAwrite);
        out8(d_i_o_port_b_handle, ~dis1);
        //printf("%x\n",(uint8_t)~dis1);
        //sleep
        pid = MsgReceivePulse(chid,&pulse,  sizeof( pulse ),NULL);

        pAwrite = in8(d_i_o_port_a_handle);
        pAwrite = pAwrite |A0 |A1 |A2; //turn off all anodes but 1
        pAwrite &= ~A3;
        out8(d_i_o_port_a_handle, pAwrite);
        out8(d_i_o_port_b_handle, ~dis0);
        //printf("%x\n",(uint8_t)~dis0);
        //sleep TODO all sleep notes need timers for 'right' freq (1/4 50hz?)
        pid = MsgReceivePulse(chid,&pulse,  sizeof( pulse ),NULL);
    }   //end while _run 
    return;
}


/**
 * @brief From the current elapsed time
 */
int Display::_refreshElapseDisplay (uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3) {
    int min, sec, sd0, sd1, sd2, sd3;
    //minutes
    min = floor(cetime/60);
    sd0 = floor(min/10);
    sd1 = floor(fmod(min,10));
    *d0 = digitToSegment(sd0);
    *d1 = digitToSegment(sd1);
    //seconds
    sec = floor(cetime - min*60 );
    sd2 = floor(sec/10);
    sd3 = floor(fmod(sec,10));
    *d2 = digitToSegment(sd2);
    *d3 = digitToSegment(sd3);
    return 1;
}

/**
 * @brief From the current distance the segments values are updated into param'd variables
 * for each 7 segment display
 */
int Display::_refreshDistDisplay(uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3) {
    double hunds,tens,ones,dec,temp;
    temp = cdistance; 
    //check if only decimal distance
    if ( (cdistance <1) && (cdistance >0) ) { 
        //blank leding zeroes
        *d0 = 0;
        *d1 = 0;
        *d2 = digitToSegment(0);
        dec = round( cdistance*10 );
        *d3 = digitToSegment (dec);
        *d2 |= SDP; //set decimal
    } else { //regular dist diplay with 0's suppressed
        //get hundreds digit
        hunds = floor(cdistance/100);
        if (hunds !=0) {
            *d0 = digitToSegment(hunds);
        } else {
            *d0 =0;
        }
        //get tens digit
        if (temp >=100) {
            temp = temp - hunds*100; //remove 100's digit
        }
        tens = floor(temp/10);
        *d1 = digitToSegment(tens);
        //get ones digit
        if (temp >=10) {
            temp = temp- tens*10;
        }
        ones = floor(temp);
        *d2 = digitToSegment(ones);
        //get tenths decimal digit
       // printf("temp:%f\n",temp); 5.2
        if (temp >0) {
            temp = temp - ones;
        }

        dec =  temp*10 ;//printf("%d ",dec);
        //printf("dec:%f\n",dec); //prints correctly
        *d2 |=SDP;
        *d3 = digitToSegment((int)dec); //TODO off by one
        //return 1; //TODO error code checking
    } //end non-suppressing leading zeroes
    return 1; //TODO error code checking
}
int flip =1;
/**
 * @brief From the current speed and the average speed the segments values 
 * are updated into param'd variables for each for the next refresh
 */
int Display::_refreshSpeedDisplay(uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3) {
    //TODO fix pulse counter for tenth decimal values as pre requirements
    double s1,s2,a1,a2; 
    //current speed dis
    if ( (cspeed <1) & (cspeed >0) ) { //less than 10, use decimal
        s1 = floor(fmod(cspeed,10));
        s2 = round(fmod(cspeed*10,10));
        *d0 = digitToSegment (s1);
        *d1 = digitToSegment (s2);
        *d0 |= SDP; //set decimal
    }else{
        //greater than 10 
        s1 = floor(cspeed/10);
        s2 = floor(fmod(cspeed,10)); //no check for over 100
        *d0 = digitToSegment(s1);
        *d1 = digitToSegment(s2);
    }
    if (flip) {
    	printf("speed: %f %f\n",s1,s2);
    }

    //avg speed
    if ( (cavg <1) & (cavg >0) ) {  //less than 10, use decimal
        a1 = floor(fmod(cavg,10));
        a2 = round(fmod(cavg*10,10));
        *d2 = digitToSegment (a1);
        *d3 = digitToSegment (a2);
        *d2 |= SDP; //set decimal
    }else{
        // 
        a1 = floor(cavg/10);
        a2 = floor(fmod(cavg,10));
        *d2 = digitToSegment(a1);
        *d3 = digitToSegment(a2);
    }
    if (flip) {
        	printf("avg: %f %f\n",a1,a2);
        }
    flip =0;
    return 1;
}

int Display::_refreshUnitDisplay(uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3) {
    *d0 = *d1 = *d2 = 0; //blank the displays
    *d3 = digitToSegment (unit+1); //TODO actual units variable
    return 1;
}

int Display::_refreshTireDisplay(uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3) {
    double hunds,tens,ones,temp;
    temp = tireSize;

    *d0 = 0 ; //never left most
    //get hundreds digit
    hunds = floor(tireSize/100);
    if (hunds !=0) {
        *d1 = digitToSegment(hunds);
    } else {
        *d1 =0;
    }
    //get tens digit
    if (temp >=100) {
        temp = temp - hunds*100; //remove 100's digit
    }
    tens = floor(temp/10);
    *d2 = digitToSegment(tens);
    //get ones digit
    if (temp >=10) {
        temp = temp- tens*10;
    }
    ones = floor(temp);
    *d3 = digitToSegment(ones);
    return 1; //TODO error code checking 
}

//
#ifdef TEST_DISPLAY
int main() {
	printf("Initializing Display\n");
	WheelSensor * wheelSensor = new WheelSensor();
	pthread_create(NULL, NULL, startWheelSensor, wheelSensor);
	PulseCounter * pulseCounter = new PulseCounter();
	pthread_create(NULL, NULL, startPulseCounter, pulseCounter);
	//wheelSensor->run();
	Display dist;
	dist.initDIO();
	dist.run();

	//TODO give display some test events with delays of course
}
#endif //TEST_DISPLAY

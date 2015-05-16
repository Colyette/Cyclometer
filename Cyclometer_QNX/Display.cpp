/**
 * @file Display.cpp
 * @brief Controls 7-segment display of Cyclometer depending on internal state
 * and variable flgs
 * @author Alyssa Colyette
 */

#include "Display.h"

#include <stdio.h>
#include <sys/neutrino.h> /* for ThreadCtl() */
#include <sys/mman.h>     /* for mmap_device_io() */
#include <hw/inout.h>     /* for in*() and out*() functions */
#include <assert.h>			/* for timer's assert */
#include <stdlib.h> //exit()
#include <math.h> 		//for floor and round functions
#include <sys/netmgr.h> 	//channel constants like ND_LOCAL_NODE



#define POLL_RATE (13) //frequency for 7 seg display ~50/4

#define TEST_DISPLAY 1 	//activates the main for display tests

void * DisplayRefreshHelper(void* instance) {
	Display* c_instance = (Display*) instance;
	printf("DisplayRefreshHelper: going into refresh thread\n");
	c_instance->refreshDisplay(); //casted to instantiated class and run main thread funct
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

#ifdef TEST_Display
    //for testing the display format without implementing the state machine
    curSubr = UNIT_SELECT;
    //values
    cspeed=60;
    cavg = 20;
    cdistance =205.1 ;
    cetime= 10000;     //in seconds
    unit=0;       //flg like 0 or 1
    tireSize=240;
#endif
}

Display::~Display(){
    _run = 0;
    //join threads..
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
}


/**
 * @brief starts the statemachine for the display.
 * @precon: DIO is initialized
 */
int run(){
    //run refresh display thread
    if (pthread_create (&segmentRunner, NULL, DisplayRefreshHelper, this)) { 
        printf("Display MainThread: error creating dio Display processing thread\n");
        return;
    }
    //check for changing states
    while (1) {
        runDisplayStateMachine();
    }
}

/**
 * @brief  run display state machine, determines next state from state transist
 */
int Display::runDisplayStateMachine () {
    //TODO
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
            converted = 0b01101111;
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
            converted = 0b01001111;
            break;
        default:
            printf("not a single digit value\n");
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
    while (_run) {
        //check state to formate diplay correctly
        //use some flg set after calc update?
        switch (curSuper) {
            case RESET:
                switch (curSubr) {
                    case UNIT_SELECT:
                        _refreshUnitDisplay(&dis0,&dis1,&dis2,&dis3);
                        dis0 = dis1 = dis2 =0; //blank the displays
                        dis3 = digitToSegment (1); //TODO actual units variable
                        break;
                    case SET_TIRE_SIZE:
                    case M_HOLD_WAIT:
                    case TIRE_AUTO:
                        _refreshTireDisplay(&dis0, &dis1, &dis2, &dis3);  //TODO error check return
                        dis0 = 0; //blank left most display
                        dis1 = digitToSegment(9);
                        dis2 = digitToSegment(8);
                        dis3 = digitToSegment(7); //TODO actual circumference with decimal masking 
                    break; //for preceding 3 states same display
                    default:
                        printf("not a valide reset state\n");
                        break; 
                }//end reset cases
                break;

            case MAIN:
                switch (curSub) {
                    case SPEED_DISPLAY:
                        //TODO fix pulse counter for tenth decimal values as pre requirements
                        _refreshSpeedDisplay(&dis0, &dis1, &dis2, &dis3);  //TODO error check return
                        dis0 = digitToSegment(9);
                        dis1 = digitToSegment(8);
                        dis2 = digitToSegment(7);
                        dis3 = digitToSegment(8);
                        break;
                    case DISTANCE_DISPLAY:
                        _refreshDistDisplay(&dis0, &dis1, &dis2, &dis3);  //TODO error check return
                        dis0 = digitToSegment(9); //(dec) 
                        dis1 = digitToSegment(8); //(dec)
                        dis2 = digitToSegment(7); //(dec)
                        dis3 = digitToSegment(6); //(dec)
                        dis3 |=SDP;
                        break;
                    case ELAPSE_DISPLAY:
                        _refreshElapseDisplay(&dis0, &dis1, &dis2, &dis3);  //TODO error check return
                        dis0 = digitToSegment(7); //(d1)
                        dis1 = digitToSegment(7); //(d2)
                        dis2 = digitToSegment(6); //(d1)
                        dis3 = digitToSegment(6); //(d2)
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
//TODO might want to separate state/display determination for better display refresh w/o num change

        //display for each digit/anode
        //assign digit value for left most
        pAwrite = in8 (d_i_o_port_a_handle);
        pAwrite = pAwrite & ~A1 & ~A2 & ~A3; //turn off all anodes but 0
        pAwrite |= A0;
        out8(d_i_o_port_a_handle, pAwrite);
        out8(d_i_o_port_b_handle, dis0);
        //sleep 
        pid = MsgReceivePulse(chid,&pulse,  sizeof( pulse ),NULL);

        //assign 2nd leftmost digit
        pAwrite = in8(d_i_o_port_a_handle);
        pAwrite = pAwrite & ~A0 & ~A2 & ~A3; //turn off all anodes but 1
        pAwrite |= A1;
        out8(d_i_o_port_a_handle, pAwrite);
        out8(d_i_o_port_b_handle, dis1);
        //sleep
        pid = MsgReceivePulse(chid,&pulse,  sizeof( pulse ),NULL);

        pAwrite = in8(d_i_o_port_a_handle);
        pAwrite = pAwrite & ~A0 & ~A1 & ~A3; //turn off all anodes but 1
        pAwrite |= A2;
        out8(d_i_o_port_a_handle, pAwrite);
        out8(d_i_o_port_b_handle, dis2);
        //sleep
        pid = MsgReceivePulse(chid,&pulse,  sizeof( pulse ),NULL);

        pAwrite = in8(d_i_o_port_a_handle);
        pAwrite = pAwrite & ~A0 & ~A1 & ~A2; //turn off all anodes but 1
        pAwrite |= A3;
        out8(d_i_o_port_a_handle, pAwrite);
        out8(d_i_o_port_b_handle, dis3);
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
    sd0 = floor( min/10);
    sd1 = floor (min-10*sd1);
    *d0 = digitToSegment(sd0);
    *d1 = digitToSegment(sd1);
    //seconds
    sec = floor (cetime - min*60 );
    sd2 = floor(sec/10);
    sd3 = floor(sec - 10*sd2);
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
        *d3 |= SDP; //set decimal
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
            temp = temp- dec*10;
        }
        ones = floor(temp);
        *d2 = digitToSegment(ones);
        //get tenths decimal digit
        if (temp >0) {
            temp = temp - ones;
        }
        dec = temp*10 ;
        *d3 = digitToSegment(dec);
        *d3 |=SDP;
        return 1; //TODO error code checking
    } //end non-suppressing leading zeroes
}

/**
 * @brief From the current speed and the average speed the segments values 
 * are updated into param'd variables for each for the next refresh
 */
int Display::_refreshSpeedDisplay(uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3) {
    //TODO fix pulse counter for tenth decimal values as pre requirements
    double s1,s2,a1,a2; 
    //current speed dis
    if ( (cspeed <10) & (cspeed >0) ) { //less than 10, use decimal
        s1 = floor(cspeed);
        s2 = round( (cspeed - floor(cspeed) )*10 );
        *d0 = digitToSegment (s1);
        *d1 = digitToSegment (s2);
        *d1 |= SDP; //set decimal
    }else{
        //greater than 10 
        s1 = floor(cspeed/10);
        s2 = floor ( cspeed - s1*10); //no check for over 100
        *d0 = digitToSegment(s1);
        *d1 = digitToSegment(s2);
    }

    //avg speed
    if ( (cavg <10) & (cavg >0) ) {  //less than 10, use decimal
        a1 = floor(cavg);
        a2 = round( (cavg - floor(cavg) )*10 );
        *d2 = digitToSegment (a1);
        *d3 = digitToSegment (a2);
        *d3 |= SDP; //set decimal
    }else{
        // 
        a1 = floor(cavg);
        a2 = floor (cavg - a1*10);
        *d2 = digitToSegment(a1);
        *d3 = digitToSegment(a2);
    }
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
	Display dist;
	dist.initDIO();

}

#endif

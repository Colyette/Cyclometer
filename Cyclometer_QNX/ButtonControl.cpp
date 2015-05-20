/**
 * @file ButtonControl.cpp
 * @brief controller for determining button presses and holds
 * author Alyssa Colyette
 */
#include <stdint.h>
#include <stdio.h>
#include <pthread.h>
#include "ButtonControl.h"

#ifdef IDK_JUST_WANT_TO_COMPILE_DISPLAY_NOW
/**
 * @brief constructor for button controller. 
 * @precon both parametered handlers need to be memory mapped beforehande
 */
//ButtonControl::ButtonControl(uintptr_t e_data_handle,uintptr_t e_control_handle) {
//    this.data_handle = e_data_handle;
//    this.control_handle = e_control_handle;
//    this.cur_state = WAIT;
//}

ButtonControl::ButtonControl() {
    //TODO default state and init dio
}
    
ButtonControl::~ButtonControl(){

}

/**
 * @brief the state machine ran to interprete events...
 */
int ButtonControl::runButtonControl(){

    while (_run) {
		switch (this.cur_state) {
			case NO_BUTTON:
				//look for a change in pin
				pollButton();
				this.cur_state = WAIT;
				break;
			case WAIT:
				//timeout
				detChain();
				break;
			case M_HOLD:
				//wait for a release of M
				break;
			case M_SS_HOLD:
				//wait for one to release or a timeout
				break;
			case ALL_HOLD:
				//wait for one to release or a timeout
				break;
			case PO_RESET:
				//throw a reset event then default beginning
				
				this.cur_state = NO_BUTTON; 
				break;
			default:
				printf("Error, not in a valid state\n");
				printf("Going back to initial state\n");
				this.cur_state = NO_BUTTON;
				break;
		}
    } 
}

int ButtonControl::detChain() { //TODO use timers?
    time_t start= time(); //todo use millisecond call
    time_t end = start + 200; //timeout
    uint8_t local_old,read; //may not be needed
    int simultPress;		//TODO really forgot what this was for...
    while ( end < time() ) { //while not the current time
        //determine if new button pressed in timeout window
        read = in8(this.data_handle) ;
        if (read ==0) { //just a button event?
            //use oldInput to determine button press
            if (oldInput&MODE_BUTTON){
#ifdef TEST_BUTTON_CONTROLLER
				printf("m_press\n");
#endif
                    //throw m_press
				throwEvent(m_press);
                return 1;
            }
            else if (oldInput&START_STOP_MODE) {
#ifdef TEST_BUTTON_CONTROLLER
				printf("ss_press\n");
#endif
                    //throw ss_press
				throwEvent(ss_press);
                return 2;
            }
            else if (oldInput&SET_BUTTOM) {
#ifdef TEST_BUTTON_CONTROLLER
				printf("s_press\n");
#endif
                    //throw s_press
				throwEvent(s_press);
                return 3;
            } else {
                printf("DIO not assigned button\n");
                return 0;
            }
        } else { //need to reset timeout
            oldInput = read;
            end += 200; //reset timout for chaining 
        } 
    }
    //should be a chained event?
   switch (read) {
        case ( (MODE_BUTTON|START_STOP_BUTTON )):
#ifdef TEST_BUTTON_CONTROLLER
				printf("m_ss_hold\n");
#endif
            //throw m_ss_hold
			throwEvent(m_ss_hold);
            simultPress =4;
            break;
        case (MODE_BUTTON| START_STOP_BUTTON | SET_BUTTON):
#ifdef TEST_BUTTON_CONTROLLER
				printf("all_hold\n");
#endif
            //throw all_hold
			throwEvent(all_hold);
            simultPress = 5;
            break;

        case (MODE_BUTTON):
#ifdef TEST_BUTTON_CONTROLLER
				printf("m_hold\n");
#endif
            //throw m_hold
			throwEvent(m_hold);
            simultPress = 6;
            break;
        default:
            printf("Unknown timeout error\nTODO\n");
            simultPress = -1;
            break;
    }

    return simultPress; //return the rec simulataneous event
}

/**
 * \brief polls to see if a button was pressed
 */
int ButtonControl::pollButton() {
    uint8_t read;
    while (read==0) {
        read = in8(this.data_handle);
    }
    oldInput = read;
    return 1;
}

/**
 * @brief initialize the DIO button pins
 */
int ButtonControl::initButtonPins(){
	int status = 0 ;
    int privity_err ;

	/* Give this thread root permissions to access the hardware */
	privity_err = ThreadCtl( _NTO_TCTL_IO, NULL );
	if ( privity_err == -1 ) {
    	fprintf( stderr, "can't get root permissions\n" );
    	status = -1;
	return 2;
	}
 	out8( d_i_o_control_handle, DIO_DIR) ;     //TODO make port A or B output for testing
    printf("Set button presses\n");
	control_handle = mmap_device_io( D_I_O_PORT_LENGTH, D_I_O_CONTROL_REGISTER ) ;
	data_handle = mmap_device_io( D_I_O_PORT_LENGTH, D_I_O_PORT_A ) ;

	_run =1; //system is now runnable
	return 1;
}

/**
 * @brief Adds the event into the event Q of the Cyclometer
 */
void ButtonControl::throwEvent(events e){
	//TODO
}

#ifdef TEST_BUTTON_CONTROLLER
int main() {
	ButtonControl bContrl;
	bContrl.initButtonPins();
	//dist.run();
	//TODO implement run function
	bContrl.runButtonControl();
	//TODO give display some test events with delays of course
}
#endif //TEST_BUTTON_CONTROLLER

#endif //IDK_JUST_WANT_TO_COMPILE_DISPLAY_NOW

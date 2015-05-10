/**
 * @file ButtonControl.cpp
 * @brief controller for determining button presses and holds
 * author Alyssa Colyette
 */
#include <stdint.h>
#include <stdio.h>
#include <pthread.h>

/**
 * @brief constructor for button controller. 
 * @precon both parametered handlers need to be memory mapped beforehande
 */
ButtonControl::ButtonControl(uintptr_t e_data_handle,uintptr_t e_control_handle) {
    this.data_handle = e_data_handle;
    this.control_handle = e_control_handle;
    this.cur_state = WAIT;
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

int ButtonControl::detChain() {
    time_t start= time(); //todo use millisecond call
    time_t end = start + 200; //timeout
    uint8_t local_old,read; //may not be needed
    int simultPress;
    while ( end < time() ) { //while not the current time
        //determine if new button pressed in timeout window
        read = in8(this.data_handle) ;
        if (read ==0) { //just a button event?
            //use oldInput to determine button press
            if (oldInput&MODE_BUTTON){
                    //throw m_press
                return 1;
            }
            else if (oldInput&START_STOP_MODE) {
                    //throw ss_press
                return 2;
            }
            else if (oldInput&SET_BUTTOM) {
                    //throw s_press
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
            //throw m_ss_hold
            simultPress =4;
            break;
        case (MODE_BUTTON| START_STOP_BUTTON | SET_BUTTON):
            //throw all_hold
            simultPress = 5;
            break;

        case (MODE_BUTTON):
            //throw m_hold
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
int pollButton() {
    uint8_t read;
    while (read==0) {
        read = in8(this.data_handle);
    }
    oldInput = read;
    return 1;
}

/**
 * @brief initializw the DI button pins
 */
int initButtonPins(){

}

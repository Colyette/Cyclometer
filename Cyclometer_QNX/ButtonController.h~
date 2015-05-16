/**
 * @file ButtonControl.h
 * @brief Controller for listening to button changes and throwing button events
 * @author Alyssa Colyette
 */
#ifndef BUTTON_CONTROL_H
#define BUTTON_CONTROL_H

#include <stdint.h>
#include <pthread.h>
//#include "c_events.h" //TODO universal event types for cyclometer

#define MODE_BUTTON         (0x01)
#define SET_BUTTON          (0x2)
#define START_STOP_BUTTON   (0x03)

class  ButtonControl{
public:
    enum bcstate {NO_BUTTON,WAIT,M_HOLD,M_SS_HOLD,ALL_HOLD,PO_RESET};     
    
    ButtonControl(uintptr_t e_data_handle,uintptr_t e_control_handle); // pass button input reg.
    ~ButtonControl();

    /**
     * @brief the state machine ran to interprete events...
     */
    int runButtonControl();

    int detChain(); //determining if a button press or hold event

    //polls the button pins
    int pollButton();
    
    //init the pins for listening to buttons
    int initButtonPins();

private:
    uint8_t oldInput;  //for storing old input values

    uintptr_t data_handle;
    uintptr_t control_handle;

    pthread_t buttonListener; //thread for reading button changes
    
    bcstate cur_state;    //the current that the machine is in
    
}
#endif  // BUTTON_CONTROL_H

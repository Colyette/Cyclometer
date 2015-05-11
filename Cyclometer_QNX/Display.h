/**
 * @file Display.h
 * @brief header file for the cyclometer display class. Implements some controller 
 * functions. Manages interface to the user.
 * @author Alyssa Colyette
 */
#ifndef DISPLAY_H
#define DISPLAY_H

#include <stdint.h>
#include <pthread.h>

//7 segment pins
//port A
#define A0  (0x00)
#define A1  (0x01)
#define A2  (0x02)
#define A3  (0x04)
//port B
#define SA  (0x00)
#define SB  (0x01)
#define SC  (0x02)
#define SD  (0x04)
#define SE  (0x08)
#define SF  (0x10)
#define SG  (0x20)
#define SDP (0x40)

//LEDs, port A
#define WHEEL_LED   (0x08)
#define AUTO_LED    (0x10)
#define UNIT_LED    (0x20)

class Display {
public:


//display states
enum display_reset_state {INIT_DATA,UNIT_SELECT,SET_TIRE_SIZE, M_HOLD_WAIT,TIRE_AUTO,NUM_R_STATES};
enum display_main_state {SPEED_DISPLAY,DISTANCE_DISPLAY,ELAPSE_DISPLAY,ELAPSE_TIMER,NUM_M_STATES},
enum display_super_state {RESET,MAIN,PO_RESET,NUM_MAIN_STATES};

//contructor and destructor for display class
Display();
~Display();

initDIO(); //open and initializes DIO on the Data ack port

//controls 7 seg display with internal variables and current state flgs
refreshDisplay();

//screen refreshing for each display mode, to get correct segment values
int _refreshDistDisplay(uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3);
int _refreshSpeedDisplay(uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3);
int _refreshElapseDisplay(uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3);
int _refreshUnitDisplay();
refreshTireDisplay();

private:
//timer for 7 segment display anode switching (MIGHT BE ABLE TO USE FOR OTHERS WITH new pulseID)
int InitializeSegmentTimer(long nsfreq, int pulseid);

//converts a digit 0-9 to encoded 7 segment value
uint8_t digitToSegment(int digit);

int _run; //internal flg for syncronizing threads...
//dio on data ack
uintptr_t d_i_o_control_handle ;     // control register for ports A, B, and C
uintptr_t d_i_o_port_a_handle ;
uintptr_t d_i_o_port_b_handle ;
 
pthread_t eTimerThread;
pthread_t segmentRunner;
display_super_state curSuper; //dictates whether to use curSub or curSubr
diplay_main_state curSub;
display_reset_state curSubr;

//values
double cspeed;
double cavg;
double cdistance;
int cetime;     //in seconds
int unit;       //flg like 0 or 1
int tireSize;   //in cm


}
#endif //DISPLAY_H

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
#include <stdio.h>
#include <sys/neutrino.h> /* for ThreadCtl() */
#include <sys/mman.h>     /* for mmap_device_io() */
#include <hw/inout.h>     /* for in*() and out*() functions */
#include <assert.h>			/* for timer's assert */
#include <stdlib.h> //exit()
#include <math.h> 		//for floor and round functions
#include <sys/netmgr.h> 	//channel constants like ND_LOCAL_NODE

#include "events.h"

//7 segment pins
//port A
#define A0  (0x01)
#define A1  (0x02)
#define A2  (0x04)
#define A3  (0x08)
//port B
#define SA  (0x01)
#define SB  (0x02)
#define SC  (0x04)//
#define SD  (0x08) //
#define SE  (0x10)
#define SF  (0x20)
#define SG  (0x40)
#define SDP (0x80)

//LEDs, port A
#define WHEEL_LED   (0x10)
#define AUTO_LED    (0x20)
#define UNIT_LED    (0x40)

//TODO make A input, B input
#define DIO_DIR		(0x00)	// Sets Port A and Port B to outputs
//For DIO port mapping
#define A_D_BASE_ADDRESS (0x280)
#define D_I_O_PORT_LENGTH (1)
#define D_I_O_CONTROL_REGISTER (A_D_BASE_ADDRESS + 0x0b)
#define D_I_O_INTERRUPT_DMA_COUNTER_CONTROL (A_D_BASE_ADDRESS +0x04)
#define D_I_O_PORT_A (A_D_BASE_ADDRESS + 0x08)
#define D_I_O_PORT_B (A_D_BASE_ADDRESS + 0x09)

class Display {
public:


//display states
//reset substates
enum display_reset_state {INIT_DATA,UNIT_SELECT, SET_TIRE_SIZE, M_HOLD_WAIT, TIRE_AUTO, NUM_R_STATES};
//main substates
enum display_main_state {SPEED_DISPLAY,DISTANCE_DISPLAY,ELAPSE_DISPLAY,NUM_M_STATES};
//substates
enum display_super_state {RESET,MAIN,PO_RESET,NUM_MAIN_STATES};

//constructor and destructor for display class
Display();
~Display();

//runs the entire state machine
int run();

int initDIO(); //open and initializes DIO on the Data ack port

//controls 7 seg display with internal variables and current state flgs
void refreshDisplay();

//run display state machine, determines next state from state transist
int runDisplayStateMachine();

//screen refreshing for each display mode, to get correct segment values
int _refreshDistDisplay		(uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3);
int _refreshSpeedDisplay	(uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3);
int _refreshElapseDisplay	(uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3);
int _refreshUnitDisplay		(uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3);
int _refreshTireDisplay		(uint8_t* d0, uint8_t* d1, uint8_t* d2, uint8_t* d3);

//elaspe timer action
int runTimer();

//passed the last event triggered into Display class
void eventUpdate( events lastEvent){curEvent = lastEvent;}

private:
//for processing if Display is in the Reset state
void _resetState();
//for processing if Display is in the Main state
void _mainState();

//for doing timeouts in a state where other triggers are possible
int startTimeout(int time_ns);
int timeout();
struct _pulse tmpulse; //for timer msg for timeout
int tmchid,tmpid; //for target of timeout timer msg passing


//set Port A and B to output
int _setPortDirection();

//gets root access for the requesting thread
int _GetRootAccess();

//timer for 7 segment display anode switching (MIGHT BE ABLE TO USE FOR OTHERS WITH new pulseID)
int _InitializeSegmentTimer(long nsfreq, int pulseid);

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
display_main_state curSub;
display_reset_state curSubr;

//values
double cspeed;
double cavg;
double cdistance;
int cetime;     //in seconds
int unit;       //flg like 0 or 1
int tireSize;   //in cm

//
int Init; //init flg for reset
int AUTO;		//manual or auto, 0 man, 1 auto
int TCalcFlg; //flag for determining if the trip calculation are on

//current event triggered
events curEvent;
};
#endif //DISPLAY_H

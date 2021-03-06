/**
 * @file: Calculations.cpp
 * @brief: Performs the calculations required for display on the Cyclometer
 * @author: Alyssa Colyette
 */
#ifndef CALCULATIONS_H
#define CALCULATIONS_H


#include "events.h"
#include "WheelSensor.h"
#include "Settings.h"
#include <math.h> 		//trip and current speed calculations
#include <assert.h>			/* for timer's assert */
#include <sys/netmgr.h> 	//channel constants like ND_LOCAL_NODE
#include <stdlib.h> //exit()

#define ACCUM_TIMEOUT_NS	(830000000)

void * startCalculations(void *);

class Calculations {
public:
	enum calcStates {ACCUM_WAIT=10,DET_MOTION,SPEED_UPDATE,DET_TRIP_CALC,TRIP_CALC_UPDATE,
PO_RESET_CALC,NUM_CALC_STATES};
	
	Calculations();
	~Calculations();

	int calcSpeed(int pulseCount);
	int calcAvgSpeed();
	int calcDistance(int pulseCount);

	
	int run();
	//det next state depending on the transition triggered 
	int runCalculationsStateMachine();

	double getLastSpeed(){return _speed;}
	double getLastAvg() {return _avg;}
	double getLastDist(){return _dist;}

	int throwEvent(events e);

	//timer for waiting until the next pulse is received
	int _InitializeAccumTimer(long nsfreq, int pulseid);

	//passed the last event triggered to Calculations class
	void eventUpdate( events lastEvent){curEvent = lastEvent;}

	//attaching the externally init WheelSensor
	void attachPulseCounter(WheelSensor* w) {pc = w;}

	//attaching the externally init Display
	void attachSettings(Settings* d){s = d;}
private:
	int _run;
	events curEvent;

	calcStates curState;	

	double _speed;
	double _avg;
	double _dist;

	//TODO these are modified from the Display class actually
	int WheelRot;
	int tireSize;
	int cetime;
	int Auto;
	int TCalcFlg;

	//reference to a pre-init WheelSensor
	WheelSensor* pc;	//for monitoring the pulse counts
	//reference to pre-init Display
	Settings* s;
};
#endif //CALCULATIONS_H

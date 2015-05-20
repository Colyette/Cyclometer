/**
 * @file: Calculations.cpp
 * @brief: Performs the calculations required for display on the Cyclometer
 * @author: Alyssa Colyette
 */
#ifndef CALCULATIONS_H
#define CALCULATIONS_H


#include "events.h"
#include "WheelSensor.h"
#include <cmath.h> 		//trip and current speed calculations

#define ACCUM_TIMEOUT_NS	(830000000)

class Calculations {
public:
	enum calcStates {ACCUM_WAIT=10,DET_MOTION,SPEED_UPDATE,DET_TRIP_CALC,TRIP_CALC_UPDATE,
PO_RESET_CALC,NUM_CALC_STATES};
	
	Calculations();
	~Calculations();

	int calcSpeed(int pulseCount);
	int calcAvgSpeed();
	int calcDistance(int pulseCount);

	
	int runCalculations();
	//det next state depending on the transition triggered 
	int runCalculationsStateMachine();

	double getLastSpeed(){return _speed;}
	double getLastAvg() {return _avg;}
	double getLastDist(){return _dist;}

	//timer for waiting until the next pulse is received
	int _InitializeAccumTimer(long nsfreq, int pulseid);

	//passed the last event triggered to Calculations class
	void eventUpdate( events lastEvent){curEvent = lastEvent;}

	//attaching the externally init WheelSensor
	void attachPulseCounter(WheelSensor* w) {pc = w;}
private:
	events curEvent;

	calcStates curState;	

	double _speed;
	double _avg;
	double _dist;

	//int WheelRot;
	//int tireSize;
	//int cetime

	//reference to a pre-init WheelSensor
	WheelSensor* pc;	//for monitoring the pulse counts
};
#endif //CALCULATIONS_H

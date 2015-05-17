/**
 * @file: Calculations.cpp
 * @brief: Performs the calculations required for display on the Cyclometer
 * @author: Alyssa Colyette
 */
#ifndef CALCULATIONS_H
#define CALCULATIONS_H

#define ACCUM_TIMEOUT_NS	(830000000)

class Calculations {
public:
	enum calcStates {ACCUM_WAIT=10,DET_MOTION,DET_TRIP_CALC,TRIP_CALC_UPDATE,
		SPEED_UPDATE,PO_RESET_CALC,NUM_CALC_STATES};
	
	Calculations();
	~Calculations();

	int calcSpeed();
	int calcAvgSpeed();
	int calcDistance();

	
	int runCalculations();
	//det next state depending on the transition triggered 
	int runCalculationsStateMachine();

	double getLastSpeed(){return _speed;}
	double getLastAvg() {return _avg;}
	double getLastDist(){return _dist;}

	//timer for waiting until the next pulse is received
	int _InitializeAccumTimer(long nsfreq, int pulseid);
private
	double _speed;
	double _avg;
	double _dist;
};
#endif //CALCULATIONS_H

/**
 * @file: Calculations.cpp
 * @brief: Holds all of the variables needed by the other classes
 * @author: Alyssa Colyette
 */
#ifndef SETTINGS_H
#define SETTINGS_H

class Settings {

public:
	Settings(){
		AUTO = 0; //manual
		//AUTO = 1; //for testing
		TCalcFlg =0; //calc off
		unit = 0; //unit kph
		tireSize = 210;
		//reset trip values
		cavg = 0;
		cdistance =0;
		cetime=0;

		WheelRot=0;


	}
	~Settings(){;}

	int getEtime(){return cetime;}
	void setEtime(int e) { cetime = e;return;}

	int getUnit(){return unit;}
	void setUnit(int u){unit=u;}

	int getTireSize(){return tireSize;}
	void setTireSize(int t) { tireSize=t;}

	int getAuto(){return AUTO;}
	void setAuto(int a){AUTO=a;}

	int getTCalcFlg(){return TCalcFlg;}
	void setTCalcFlg(int cflg){ TCalcFlg = cflg;}

	double getCurSpeed(){return cspeed;}
	void setCurSpeed(double cs) {cspeed =cs;}

	double getAvgSpeed(){return cavg;}
	void setAvgSpeed(double as){cavg = as;}

	double getDist(){return cdistance;}
	void setDist(double d) { cdistance = d;}

	int getWheelRot(){return WheelRot;}
	void setWheelRot(int w){WheelRot = w;}


private:
	int cetime;     //in seconds
	int unit;       //flg like 0 or 1
	int tireSize;   //in cm

	int AUTO;		//manual or auto, 0 man, 1 auto
	int TCalcFlg; 	//flag for determining if the trip calculation are on

	//externally modified
	double cspeed;
	double cavg;
	double cdistance;
	int WheelRot;



};
#endif //SETTINGS_H

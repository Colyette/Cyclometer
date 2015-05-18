

#include "Cyclometer.h"

//inilize static mutex eventQ control
std::recursive_mutex Cyclometer::eventQ_mutex;

Cyclometer::Cyclometer(){

}

int Cyclometer::initCyclometer(){
	display = Display(); //TODO init and run
	calculations = Calculations(); //TODO init and run
	buttonCntrl = ButtonController(); //TODO init and run

	//TODO Pass each class required values for updates?
	while (1) {
		//give Diplay required values

		//give Calculations required values
		
		//broadcast next event

	}

}

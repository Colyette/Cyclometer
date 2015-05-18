#include <cstdlib>
#include <iostream>
#include <pthread.h>
#include "WheelSensor.h"

void *WheelHelper(void* instance) {
	WheelSensor* c_instance = (WheelSensor*) instance;
	printf("WheelHelper: going into interrupt thread\n");
	c_instance->run(); //casted to instantiated class and run main thread funct
	return 0 ;
}

int main(int argc, char *argv[]) {
	std::cout << "Welcome to the QNX Momentics IDE" << std::endl;
	pthread_t wThread;
	WheelSensor w = WheelSensor();
	//run refresh display thread
	if (pthread_create (&wThread, NULL,startWheelSensor, &w)) {
	        printf("WheelSensor MainThread: error running thread\n");
	        return -1;
	 }

	for (int i = 0; i<10; i++){
		sleep(1);
		printf("Cnt:%d\n",w.getCount());

	}
	pthread_join(wThread,NULL);
	return EXIT_SUCCESS;
}

//int main() {
//	Display dist;
//	dist.initDIO();
//
//}



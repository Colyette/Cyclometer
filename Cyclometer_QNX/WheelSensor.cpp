/*
 * WheelSensor.cpp
 *
 *  Created on: Feb 4, 2013
 *      Author: rfd6477
 *
 *      Description: The wheel sensor class monitors
 *      the DIO port 25 and handles the interrupts.
 *      When an interrupt occurs the pulse count variable
 *      is incremented and stored for others to retrieve.
 * @author Alyssa Colyette
 * @brief modified for Cyclometer implementation for outside clearing
 */

#include "WheelSensor.h"
#include <cstdlib>
#include <iostream>
#include <pthread.h>

//#define TEST_WHEEL_SENSOR 1 //WheelSensor Testing

const struct sigevent * interruptReceived(void *arg, int id)
{
	uintptr_t clear_handle;
	clear_handle = mmap_device_io( PORT_LENGTH, CLEAR_ADDRESS );

	((WheelSensor *)arg)->updateCount();
	out8( clear_handle, CLEAR );
	//printf("Wheel Signal");
	return NULL;
}

WheelSensor::WheelSensor() {
	int privity_err;
	uintptr_t ctrl_handle;
	uintptr_t clear_handle;
//TODO MIGHT interfer with DIO in Display class... init after Display?
	privity_err = ThreadCtl( _NTO_TCTL_IO, NULL );
	if ( privity_err == -1)
	{
		printf( "Can't get root permissions\n");
	}

	// Get a handle to Interrupt Control Register
	ctrl_handle = mmap_device_io( PORT_LENGTH, CTRL_ADDRESS );
	clear_handle = mmap_device_io( PORT_LENGTH, CLEAR_ADDRESS );

	if ( ctrl_handle == MAP_DEVICE_FAILED ) {
		perror( "control map failed" );

	}

	out8( ctrl_handle, INIT_BIT );
	out8( clear_handle, CLEAR );

	_pulseCount=0;
	_pulseHist = 0;
	_run =1;
	printf("Initialized WheelSensor\n");
}

WheelSensor::~WheelSensor() {
	// TODO Auto-generated destructor stub
}

/* Starts the thread. This is the function that should be called
 * by pthread_create */
void * startWheelSensor(void * sensor)
{
	((WheelSensor *)sensor)->run();
	return NULL;
}

/* Runs the logic for the Wheel Sensor */
void WheelSensor::run()
{
	printf("Starting Wheel Sensor\n");
	_interruptID = InterruptAttach(DIO_IRQ, interruptReceived, this, sizeof(this), 0);
	//_interruptID = InterruptAttach(0, WheelinterruptReceived, this, sizeof(this), 0);
	if (_interruptID == -1) {
		fprintf(stderr, "can't attach to IRQ %d\n", DIO_IRQ);
		perror(NULL);
	}
	

	while(_run){
		//sleep(1); //TODO might be processor intensive without spacing...
		if (_pulseCount != _pulseHist)
		{
			_pulseHist = _pulseCount;
		}
		//_pulseCount = 0; //doing outside reset
	}
}

int WheelSensor::getCount()
{
	return _pulseHist;
	//return _pulseCount;
}

void WheelSensor::clearCount() {
	_pulseCount =0;
}

void WheelSensor::updateCount()
{
	_pulseCount++;
}
#ifdef TEST_WHEEL_SENSOR
int main(int argc, char *argv[]) {
	std::cout << "Welcome to the QNX Momentics IDE" << std::endl;
	pthread_t wThread;
	WheelSensor w = WheelSensor();
	//run refresh display thread
	if (pthread_create (&wThread, NULL,startWheelSensor, &w)) {
	        printf("WheelSensor MainThread: error running thread\n");
	        return -1;
	 }
	printf("Polling 10 times after a second in between\n");
	for (int i = 0; i<10; i++){
		sleep(1);
		printf("Cnt:%d\n",w.getCount());

	}
	printf("Now polling 10 times after a second in between with clear\n");
	for (int i = 0; i<10; i++){
		sleep(1);
		printf("Cnt:%d\n",w.getCount());
		w.clearCount();
	}
	w.killRun();
	printf("Done\n");
	pthread_join(wThread,NULL);
	return EXIT_SUCCESS;
}
#endif //TEST_WHEEL_SENSOR



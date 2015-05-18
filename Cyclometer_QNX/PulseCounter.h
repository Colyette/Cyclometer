/**
 * @file: PulseCounter.h
 * @brief: Counts the amount of pulses from the magnetic sensor
 * @author: Alyssa Colyette
 */

#include <pthread.h>
#include <unistd.h>
#include <stdio.h>
#include <hw/inout.h>
#include <time.h>
#include <stdint.h>
#include <sys/neutrino.h>
#include <sys/mman.h>
#include <stdlib.h>
#include <atomic.h>		/*atomic_add for pulse counting*/

/* The Neutrino IO port used here corresponds to a */
/* single register which is one byte long */
#define PORT_LENGTH 1
/* The first parallel port usually starts at 0x378. Each */
/* parallel port is three bytes wide. The first byte */
/* is the Data register, the second byte is the status */
/* register and the third byte is the control register */
#define DATA_ADDRESS 0x378
#define STATUS_ADDRESS 0x379  /* added by Roy */
#define CTRL_ADDRESS 0x37a
/* bit 2 = printer initialization (high to initialize) */
/* bit 4 = hardware IRQ (high to enable) */
#define INIT_BIT 0x04
#define INTR_BIT 0x10
#define PARALLEL_IRQ 0x07 /* parallel port’s interrupt vector */
 
#define LOW 0x00
#define HIGH 0xFF
#define MAX_COUNT 60

/**IRQ for mag pulses*/
const struct sigevent *interruptReceived(void *arg, int id);
volatile unsigned _pulseCount; //counts the pulses via IRQ, need to make when clearing
class PulseCounter {
public:
PulseCounter();
~PulseCounter();

//initialize port for IRQ
int init_p_port(); 

//attaches the interrupt of notifiying pulses
int run();

void clearPulseCount(){_pulseCount =0;}

//unsigned readPulseCount(){return _pulseCount;}

private:
//TODO move globals
//volatile unsigned _pulseCount; //counts the pulses via IRQ, need to make when clearing
int interruptID; 
};

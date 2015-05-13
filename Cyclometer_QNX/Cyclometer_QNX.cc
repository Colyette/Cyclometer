#include <cstdlib>
#include <iostream>

//#define INPUT_IRQ (7)

#include <stdlib.h> 
#include <stdio.h>
#include <unistd.h>     /* for sleep() */
#include <stdint.h>
#include <hw/inout.h>   /* for in*() and out*() functions */
#include <sys/neutrino.h>   /* for ThreadCtl() */
#include <sys/mman.h>   /* for mmap_device_io() */
#include <atomic.h>		/*atomic_add for pulse counting*/

#ifdef IDK_JUST_WANT_TO_COMPILE_DISPLAY_NOW

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

//TODO move defines
/* -------------------------------------------- */
//TODO move globals
volatile unsigned _pulseCount; //counts the pulses via IRQ, need to make when clearing
//use atomic_clr( &_pulseCount, 0xFF); to clear all bits in the values

int interruptID; 

int init_p_port() {
    int privity_err;
    uintptr_t ctrl_handle;
    uintptr_t data_handle;
    uintptr_t status_handle;  /* added by Roy */
    int count;
    char status_byte;  /* added by Roy */
    printf("Welcome to the Momentics IDE\n");   
    /* Give this thread root permission to access */
    /* the hardware */
    privity_err = ThreadCtl( _NTO_TCTL_IO, NULL );
    if ( privity_err == -1)
    {
        fprintf( stderr, "can't get root permissions\n");
        return -1;
    }
    /* Get a handle to the parallel port's Control Register */
    ctrl_handle = mmap_device_io( PORT_LENGTH, CTRL_ADDRESS );
    if ( ctrl_handle == MAP_DEVICE_FAILED ) {
        perror( "control map failed" );
        return EXIT_FAILURE;
    }
    /* Get a handle to the parallel port's Control Register */
    status_handle = mmap_device_io( PORT_LENGTH, STATUS_ADDRESS );
    if ( status_handle == MAP_DEVICE_FAILED ) {
        perror( "status map failed" );
        return EXIT_FAILURE; 
    }
    /* INitialize the parallel port */
    out8( ctrl_handle, INTR_BIT);
    
    /* Get a handle to the parallel port's Data Register */
    data_handle = mmap_device_io( PORT_LENGTH, DATA_ADDRESS );
    if ( data_handle == MAP_DEVICE_FAILED ) {
        perror( "data map failed" );
        return EXIT_FAILURE;
    }   
#ifdef TEST
    for ( count = 0; count < MAX_COUNT; count++ )
    {
        /* Output a byte of lows to the data lines */
        out8( data_handle, LOW );
        printf( "Low\n" );
        status_byte = in8( status_handle);
        printf( "status byte = %x \n", status_byte ); /* added by Roy */
        sleep( 1 );
        /* Output a byte of highs to the data lines */
        out8( data_handle, HIGH );
        printf( "High\n" );
        status_byte = in8( status_handle);
        printf( "status byte = %x \n", status_byte ); /* added by Roy */
        sleep( 1 );
    }
#endif
    /* Enable interrupts on the parallel port */
    out8( ctrl_handle, INTR_BIT ); // just the ack bit?

    return 0;
}


/**IRQ for mag pulses*/
const struct sigevent *interruptReceived(void *arg, int id) {
    atomic_add_value( &_pulseCount, 1 );
    return NULL;
} 

int main() {
    printf("Welcome to the Momentics IDE\n");
    if (init_p_port() ) {
        printf("Parallel Port not initialized properly\n");
        return EXIT_FAILURE;
    } 
    // attach interrupt for ack pin
    interruptID = InterruptAttach(PARALLEL_IRQ, interruptReceived, this,
        sizeof(this), 0);
    if (interruptID == -1) {
        fprintf(stderr, "can't attach to IRQ %d\n", PARALLEL_IRQ);
        perror(NULL);
        exit(EXIT_FAILURE);
    }

    //start worker threads

    //

    return 0;
}
#endif //IDK_JUST_WANT_TO_COMPILE_DISPLAY_NOW

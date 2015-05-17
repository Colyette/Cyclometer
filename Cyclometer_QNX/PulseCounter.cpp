/**
 * @file: PulseCounter.cpp
 * @brief: Counts the amount of pulses from the magnetic sensor
 * @author: Alyssa Colyette
 */

#include "PulseCounter.h"

/**IRQ for mag pulses*/
const struct sigevent *interruptReceived(void *arg, int id) {
    atomic_add_value( &_pulseCount, 1 );
    return NULL;
} 

PulseCounter::PulseCounter() {
	init_p_port();
}

PulseCounter::~PulseCounter() {
	printf("Deconstructing PulseCounter\n");
}


int PulseCounter::init_p_port() {
    int privity_err;
    uintptr_t ctrl_handle;
    uintptr_t data_handle;
    uintptr_t status_handle;  /* added by Roy */
    int count;
    char status_byte;  /* added by Roy */
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

int PulseCounter::run() {
	interruptID = InterruptAttach(PARALLEL_IRQ, interruptReceived, this, sizeof(this), 0);
	if (interruptID == -1) {
		fprintf(stderr, "can't attach to IRQ %d\n", PARALLEL_IRQ);
		perror(NULL);
		return -1;
	}
	return 1;
	
}


#ifdef TEST_PULSECOUNTER
int main() {
	PulseCounter pc = PulseCounter();

    printf("Welcome to the Momentics IDE\n");
    if (pc.init_p_port() ) {
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
#endif //TEST_PULSECOUNTER

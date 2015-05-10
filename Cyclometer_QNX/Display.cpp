/**
 * @file Display.cpp
 * @brief Controls 7-segment display of Cyclometer depending on internal state
 * and variable flgs
 * @author Alyssa Colyette
 */
#include "Display.h"

#include <stdio.h>

//contructor and destructor for display class
Display::Display(){
    curSuper = RESET;
    curSub = INIT_DATA;
    curSubr = NUM_M_STATES;
    //init DIO here?
    this._run = 1;
}

Display::~Display(){
    this._run =0;
    //join threads..
}

uint8_t digitToSegment(int digit) {
    uint8_t converted;
    switch (digit) {
        case 0:
            converted = 0b00111111;
            break;
        case 1:
            converted = 0b00000110;
            break;
        case 2:
            converted = 0b01011011;
            break;
        case 3:
            converted = 0b01001111;
            break;
        case 4:
            converted = 0b01100110;
            break;
        case 5:
            converted = 0b01101111;
            break;
        case 6:
            converted = 0b01111101;
            break;
        case 7:
            converted = 0b00000111;
            break;
        case 8:
            converted = 0b01111111;
            break;
        case 9:
            converted = 0b01001111;
            break;
        default:
            printf("not a single digit value\n");
            converted = 0;
            break;
    }
    return converted;
}

//controls 7 seg display with internal variables and current state flgs
Display::refreshDisplay(){
        uint8_t dis0,dis1,dis2,dis3; //l to r
        int i; 
        uint8_t pAwrite;
//TODO set up DIO
    while (_run) {
        //check state to formate diplay correctly
        switch (curSuper) {
            case RESET:
                switch () {

                }//end reset cases
                break;

            case MAIN:
                switch () {

                } //end main cases
                
                break;
            case PO_RESET:
                
                break;
            default:
                printf("Not in a valid display state\n");
                break;
        } 
//TODO might want to separate state/display determination for better display refresh w/o num change

        //display for each digit/anode
        //assign digit value for left most
        pAwrite = in8 (d_i_o_port_a_handle);
        pAwrite = pAwrite & ~A1 & ~A2 & ~A3; //turn off all anodes but 0
        pAwrite != A0;
        out8(d_i_o_port_a_handle, pAwrite);
        out8(d_i_o_port_b_handle, dist0);
        //sleep 
        //assign 2nd leftmost digit
        pAwrite = in8(d_i_o_port_a_handle);
        pAwrite = pAwrite & ~A0 & ~A2 & ~A3; //turn off all anodes but 1
        pAwrite |= A1;
        out8(d_i_o_port_a_handle, pAwrite);
        out8(d_i_o_port_b_handle, dist1);
        //sleep
        pAwrite = in8(d_i_o_port_a_handle);
        pAwrite = pAwrite & ~A0 & ~A1 & ~A3; //turn off all anodes but 1
        pAwrite |= A2;
        out8(d_i_o_port_a_handle, pAwrite);
        out8(d_i_o_port_b_handle, dist2); 
        //sleep
        pAwrite = in8(d_i_o_port_a_handle);
        pAwrite = pAwrite & ~A0 & ~A1 & ~A2; //turn off all anodes but 1
        pAwrite |= A3;
        out8(d_i_o_port_a_handle, pAwrite);
        out8(d_i_o_port_b_handle, dist3);
        //sleep TODO all sleep notes need timers for 'right' freq (1/4 50hz?)
    }   //end while _run 
}

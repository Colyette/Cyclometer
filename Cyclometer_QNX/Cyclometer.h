

#ifndef CYCLOMETER_H
#define CYCLOMETER_H

#include "Display.h"
#include "Calculations.h"
#include "ButtonController.h"
#include "events.h"
//for shared event q
#include <queue>
#include <deque>
#include <mutex>        //for recursive mutex
//TODO globally define events

class Cyclometer {
public:
Cyclometer();
~Cyclometer();

int initCyclometer();

std::recursive_mutex* getQmutex() {return &eventQ_mutex;}
std::queue<event>* getQ() {return &eventQ;}




private:
Display display;
Calculations calculations;
ButtonController buttonCntl;

//Event Q
std::queue<event> eventQ;
//mutex for q handling
static std::recursive_mutex eventQ_mutex;

};
#endif //CYCLOMETER_H

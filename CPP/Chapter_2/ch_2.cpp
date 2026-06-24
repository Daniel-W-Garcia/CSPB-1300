#include <iostream>
#include "ch_2.h"


string get_user_input() {

    string name; // declaring a variable without initializing it
    cout << "Please enter your name: ";
    cin >> name; //variable is filled here
    cout << name;
    return name;
}
#include <iostream>
#include <cmath>
using namespace std;

float getSquare(float a)
{
    float g1 = a/2.0f;
    float g2 = 0;
    float square = 0;

    while (abs(g1-g2) >= .005f)
    {
        g2 = (a/g1 + g1)/2.0f;
        float temp = g1;
        g1 = g2;
        g2 = temp;
    }
    square = g1;
    return square;
}

 string printBox(int row, int col)
{
    int i = 0;
    int j = 0;
    while (j < row)
        cout << "\u25A0";
        

    return "complete";
}

string get_user_input() {

    string name; // declaring a variable without initializing it
    cout << "Please enter your name: ";
    cin >> name; //variable is filled here
    //cout << "Your name is: " + name << endl;
    return name;
}


int main() {

    //string pattern = printBox(10, 1);
    string name = get_user_input();
    cout << "Your name is: " + name;

    return 0;
}

# Data Types

## Variables

- C++ is a Type Safe language
  - Variables must define their data type upon initialization
  - int var_name = 0  

- Variable Rules:  
  - can start with '_' or a letter
  - CANNOT start with number or special char
  - cannot contain reserved words or chars or spaces

- Assignment statement vs Variable Definition
  - int cans_per_pack = 6 is a definition. It initializes a variable in memory
  - cans_per_pack = 8 is an assignment statement. It assigns a value to an EXISTING variable

### Constants

- When a variable is assigned with const, its value can never be changed
  - const double PI = 3.14 UPPERCASE convention for constants

### Comments

- Comments can be used to explain the significance of a line or the purpose of a block of code
- Comment help make code much more human-readable  
- Single line comments start with '//'
- Block comments start with /* and end */

## Arithmetic

- When using division '/' if both numbers are ints, the result will be an int with no decimals
  - As long as either of the nums is a float, then division works as normal

### Modulus
- The remainder of division
- n % 10 is always the last digit of n
- n % 100 is the last 2 digits...and so on
- -n % 10 is the last digit of n as a negative (-x)

### Floats to Ints
- adding .5 to any float before casting to an int will round it to nearest whole number
  - int dollas = 2.55 + .5
    - 3.05 as an int is 3

### Powers and Roots:
- add '#include <cmath>' as a header to use built in functionss 
  - sqrt(x) pow(num, power) 

## Input and Output

### Input

- The '<<' operator combined with 'cin' keyword allow to collect user input
  - Often a string 'prompt' instructs the user what info is required

```c++
#include <iostream> // needed to use built in methods
string get_user_input() {

    string name; // declaring a variable without initializing it
    cout << "Please enter your name: ";
    cin >> name; //variable is filled here
    cout << name;
    return name;
}
```

### Output

```c++
#include <iomanip> // needed to use any of the manipulator functions
```
- manipulators are functions that format an output
  - fixed(x) and setprecision(x) are two built in functions that act as manipulators
    - fixed is sticky and forces any scientific notation into decimals
    - setprecision is the number of digits after a decimal pace
      - setprecision applies to all floating point numbers in the statement 
  - setw(x) is used to line data up. Where x is the total width of the output
    - this includes all characters and spaces
      - this will line everything up to the right (right justified)
      - setw() applies ONLY to the next value
      - if setw() is not wide enough to contain the output, it is ignored
- By default digits are printed to 6 significant digits
  - cout << 15.12345678 -> 15.1234

## Strings

```c++
#include <string>
```
- Strings are automatically initialed with an empty string if no value is given
- A string literal is the actual string (the part in quotes)
- Concatenate strings with the '+' operator
- you can use cout to read a string from the console
  - cout << string_name << endl;

### cin to assign a string leteral to a string variable

```c++
#include <string>

    cout << "Please enter your full name: ";
    string first;
    string last;
    cin >> first >> last;
    string full_name = last + ", " + first;
```

### 'length' function
- invoked with dot '.' notation
  - these are known as a <strong> Member Functions</strong>

```c++
string name = "Daniel"
int name_length = name.length() // length returns an int
```

### 'substr' function
```c++
#inlcude <string>
// substr(start, length)
string name = "Daniel"
string sub_name = name.substr(1, 3); //"ani"
```

### Unicode

- A standardization of the worlds different characters and alphabets consisting of approx 100,000 characters in total

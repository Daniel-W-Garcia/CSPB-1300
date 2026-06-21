# Review Exercises

- <strong><u>R1.1</strong></u> Explain the difference between using a computer program and programming a computer.
    - You program a computer to execute an algorithm.  
<br/>
- <strong><u>R1.2</strong></u> Which parts of a computer can store program code? Which can store user data?
<br/><br/>

- <strong><u>R1.3</strong></u> Which parts of a computer serve to give information to the user? Which parts take user input?
  <br/><br/>
- <strong><u>R1.4</strong></u> A toaster is a single-function device, but a computer can be programmed to carry out different tasks. Is your cell phone a single-function device, or is it a programmable computer?
  <br/><br/>
- <strong><u>R1.5</strong></u> Explain two benefits of using C++ over machine code.
  <br/><br/>
- <strong><u>R1.6</strong></u> On your own computer or on your lab computer, find the exact location (folder or directory name) of

  - a. The sample file hello.cpp (after you saved it in your development environment).
  - b. The standard header file <iostream>.
<br/><br/>
- <strong><u>R1.7</strong></u> What does this program print?
```c++
#include <iostream>
using namespace std;

int main()
{
cout << "6 * 7 = " << 6 * 7 << endl;
return 0;
}
```
<br/><br/>
- <strong><u>R1.8</strong></u> What does this program print? Pay close attention to spaces.  

```c++
#include <iostream>
using namespace std;

int main()
{
   cout << "Hello" << "World" << endl;
   return 0;
}
```
<br/><br/>
- <strong><u>R1.9</strong></u> What does this program print?
```c++

#include <iostream>
using namespace std;

int main()
{
   cout << "Hello" << endl << "World" << endl;
   return 0;
}
```

<br/><br/>
- <strong><u>R1.10</strong></u> Write three versions of the hello.cpp program that have different compile-time errors. Write a version that has 
a run-time error. &nbsp;
<!-- -->
- <strong><u>R1.11</strong></u> How do you discover compile-time errors? How do you discover run-time errors?
<!-- -->
- <strong><u>R1.12</strong></u> Write an algorithm to settle the following question: A bank account starts out with \$10,000. Interest is compounded monthly at 6 percent per year (0.5 percent per month). Every month, \$500 is withdrawn to meet college expenses. After how many years is the account depleted?
<!-- -->
- <strong><u>R1.13</strong></u> Consider the question in Exercise - R1.12. Suppose the numbers (\$10,000, 6 percent, \$500) were user selectable. Are there values for which the algorithm you developed would not terminate? If so, change the algorithm to make sure it always terminates.
<!-- -->
- <strong><u>R1.14</strong></u> In order to estimate the cost of painting a house, a painter needs to know the surface area of the exterior. Develop an algorithm for computing that value. Your inputs are the width, length, and height of the house, the number of windows and doors, and their dimensions. (Assume the windows and doors have a uniform size.)
<!-- -->
- <strong><u>R1.15</strong></u> You want to decide whether you should drive your car to work or take the train. You know the one-way distance from your home to your place of work, and the fuel efficiency of your car (in miles per gallon). You also know the one-way price of a train ticket. You assume the cost of gas at \$4 per gallon, and car maintenance at 5 cents per mile. Write an algorithm to decide which commute is cheaper.
<!-- -->
- <strong><u>R1.16</strong></u> Suppose you put your younger brother in charge of backing up your work. Write a set of detailed instructions for carrying out his task. Explain how often he should do it, and what files he needs to copy from which folder to which location. Explain how he should verify that the backup was carried out correctly.
<!-- -->
- <strong><u>R1.17</strong></u> The cafeteria offers a discount card for sale that entitles you, during a certain period, to a free meal whenever you have bought a given number of meals at the regular price. The exact details of the offer change from time to time. Describe an algorithm that lets you determine whether a particular offer is a good buy. What other inputs do you need?
<!-- -->
- <strong><u>R1.18</strong></u> Write pseudocode for an algorithm that describes how to prepare Sunday breakfast in your household.
<!-- -->
- <strong><u>R1.19</strong></u> The ancient Babylonians had an algorithm for determining the square root of a number a. Start with an initial guess of a / 2. Then find the average of your guess g and a / g. That’s your next guess. Repeat until two consecutive guesses are close enough. Write pseudocode for this algorithm.
<!-- -->
<br/><br/>
- <strong><u>R1.20</strong></u> Write an algorithm to create a tile pattern composed of black and white tiles, with a fringe of black tiles all around and two or three black tiles in the center, equally spaced from the boundary. The inputs to your algorithm are the total number of rows and columns in the pattern.
```markdown
⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬜  
⬜⬛⬛⬜⬜⬜⬛⬛⬜  
⬜⬛⬛⬛⬛⬛⬛⬛⬜  
⬜⬛⬛⬛⬛⬛⬛⬛⬜  
⬜⬜⬜⬜⬜⬜⬜⬜⬜
```

> <em>Note: The above uses black boxes, but they should really just be blank spaces. I couldnt figure out how to make it look pretty any other way. </em>
> 

<br/>


- <strong><u>R1.21</strong></u> Write an algorithm to create a tile pattern composed of alternating black and white squares, like this:
<!-- -->
```markdown
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬜⬛⬜⬛⬛⬛⬛⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬜⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬜⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬛⬛⬛⬛⬜⬛⬜
⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜

```
&nbsp;
<br/>
- <strong><u>R1.22</strong></u> Write an algorithm that allows a robot to mow a rectangular lawn, provided it has been placed in a corner, like this:

```markdown
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜
⬜🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜
⬜🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜
⬜🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜
⬜🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜
⬜🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜
⬜🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
```


  - The robot (marked as R) can:
  
    - Move forward by one unit.
    - Turn left or right.
    - Sense the color of the ground one unit in front of it.
<!-- -->
<br/>

- <strong><u>R1.23</strong></u> Consider a robot that is placed in a room. The robot can:

  - Move forward by one unit.
  - Turn left or right.
  - Sense what is in front of it: a wall, a window, or neither.

  >Write an algorithm that enables the robot, placed anywhere in the room, to count the number of windows. For example, in the room at right, the robot (marked as R) should find that it has two windows.

<br/><br/>
- <strong><u>R1.24</strong></u> Consider a robot that has been placed in a maze. The right-hand rule tells you how to escape from a maze: Always have the right hand next to a wall, and eventually you will find an exit. The robot can:

  - Move forward by one unit.
  - Turn left or right.
  - Sense what is in front of it: a wall, an exit, or neither.

  >Write an algorithm that lets the robot escape the maze. You may assume that there is an exit that is reachable by the right-hand rule. Your challenge is to deal with situations in which the path turns. The robot can’t see turns. It can only see what is directly in front of it.
<br/>
- <strong><u>Business R1.25</strong></u> Suppose you received a loyalty promotion that lets you purchase one item, valued up to \$100, from an online catalog. You want to make the best of the offer. You have a list of all items for sale, some of which are less than \$100, some more. Write an algorithm to produce the item that is closest to \$100. If there is more than one such item, list them all. Remember that a computer will inspect one item at a time––it can’t just glance at a list and find the best one.
  <br/><br/>
- <strong><u><p>Engineering R1.26</strong></u> A television manufacturer advertises that a television set has a certain size, measured diagonally. You wonder how the set will fit into your living room. Write an algorithm that yields the horizontal and vertical size of the television. Your inputs are the diagonal size and the aspect ratio (the ratio of width to height, usually 16 : 9 for television sets).
  <br/><br/>
- <strong><u>Engineering R1.27</strong></u> Cameras today can correct “red eye” problems caused when the photo flash makes eyes look red. Write pseudocode for an algorithm that can detect red eyes. Your input is a pattern of colors, such as that shown below.</p> <br/>

  <p>You are given the number of rows and columns. For any row or column number, you can query the color, which will be red, black, or something else. If you find that the center of the black pixels coincides with the center of the red pixels, you have found a red eye, and your output should be “yes”. Otherwise, your output is “no”.</p> <br/><br/>

- <strong><u>Engineering R1.28</strong></u> The San Francisco taxi commission set the following rates for 2017:
  - First 1/5th of a mile: \$3.50
  - Each additional 1/5th of a mile or fraction thereof: \$0.55
  - Each minute of waiting or traffic delay: \$0.55 </br>
    The charge for “waiting or traffic delay” applies instead of the mileage charge for each minute in which the speed is slower than the break-even point. The break-even point is the speed at which 1/5th of a mile is traversed in one minute.
   >Develop an algorithm that yields the fare for traveling a given distance in a given amount of time, assuming that the taxi moves at a constant speed.
   >
<br/>

- <strong><u>Engineering R1.29</strong></u> Suppose you know how long it takes a car to accelerate from 0 to 60 miles per hour. Develop an algorithm for computing the time required to travel a given distance (for example 5 miles), assuming that the car is initially at rest, accelerates to a given speed (for example 25 miles per hour), and drives at that speed until the distance is covered. Hint: An object that starts at rest and accelerates at a constant rate a for t seconds travels a distance of s = 1/2at2.</p><br/>

- <strong><u>Engineering R1.30</strong></u> Taxi meters measure the distance traveled by counting the number of revolutions of an axle. The meter is initialized by driving a known distance. A disreputable taxi driver tricks his customers into paying more per trip. He does this by slightly deflating his taxi’s tires after the meter has been initialized, so that they have a smaller radius. This way, the tire will have a greater number of revolutions per trip, making each trip appear to be a greater number of miles.<br/>
  
  >Develop an algorithm for computing what the deflated tire radius must be if the taxi driver would like a short x-mile taxi ride to appear to be a longer y-mile taxi ride. Inputs are the proper tire radius R and the distances x and y.

# ArtificialInteligence
## Problem statement
A traffic intersection can be approached by vehicles from the North, from the East and from the West.

![Captura de pantalla 2023-05-04 100121](https://user-images.githubusercontent.com/98906745/236173559-c10b7bc0-f76d-4790-b1d5-08b4e48308ed.png)

The flow of vehicles in each direction encounters a traffic light before reaching the intersection, which can be either green or red. An operator must select every 20 seconds which of the three traffic lights to turn green: the other two will automatically turn red.
Sensors measure the level of traffic in each direction prior to the intersection. The values can be: High or Low. When the traffic light in one direction is green, the level will normally stay the same or go down, only very occasionally increasing. When the traffic light is closed, the level stays the same or rises.
We want to design an automaton that opens the appropriate traffic light at each cycle following the optimal policy of the corresponding MDP. The target situation is that traffic in all three directions is Low. In such a situation, the automaton stops working.
## Input data
Historical data is available for situations where we know:

  · The traffic levels at the start of the 20-second cycle.
  
  · The traffic light that remained green during that period.
  
  · The traffic levels at the end of the cycle. 
  
The historical data are in a file. Each line contains 7 values separated by ";". The first three are the traffic levels at the beginning of the 20 seconds in the order North, East, West, the fourth is the traffic light that stays green during those 20 seconds and the last three are the traffic levels at the end.
For example, the line:
High;High;Low;E;High;High;High
indicates that we had High traffic coming in from the North and East and Low traffic from the West, the traffic light controlling incoming traffic from the East was green and within 20 seconds traffic was High in all three directions.
## Project development
The main objective of the project is to obtain the optimal policy for the automaton. The first step will be to identify the tasks necessary to reach this goal. Some tasks may require the development of software. The programs should be as generic as possible, using constants to adapt them to this particular project. The programming language must be Python. 
The student must answer the following questions:

  · The input data does not include any cases where the starting situation was low traffic level in all three directions. Is this normal? If you had this kind of data, what would happen or what should we have done?
  
  · The statement does not say anything about the cost of the actions. What reasonable assumption could we make?
  
  · What are the expected values of the states? Provide the values to six decimal places. The precision must be greater than one thousandth.
  
  · What is the optimal policy?
  
  · If we had also had incoming traffic from the South and for each direction we had measured traffic at 5 levels instead of 2, what would have changed in the problem?

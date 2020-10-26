# Exam 1 Take-Home Project

In this project you will implement a code to simulate the motion of non-interacting particles inside a box. 
We will discretize time into small time interval (timestep) and will update the position and velocity of each particle according to simple physical laws. 
We will use the animate module of matplotlib to visualize the particles during their motions.

The project is organized into four tasks. Although each following task can be implemented as a modification of the same starting code, 
in order to simplify and guide your work four different python files have been created in this repository. The files contain comments with more
details on the specific tasks that are required by this project.

TASKS:
1. Starting from the task1.py program, implement a function to move a particle inside a one-dimensional box. The particle follows a uniform velocity motion along the x axis. The particle has no interactions with other objects, but it can undergo elastic collisions with the sides of the box. 
2. Starting from the task2.py program, and the developments in the previous task, extend the program to account for a variable number of particles. Initialize the positions and velocities of the particles using random numbers. 
3. Starting from the task3.py program, and the developments in the previous two tasks, extend the program to model non-interacting particles in two dimensions. Initialize the positions and velocities in the two directions using random numbers.
4. Starting from the task4.py program, and the developments in the previous three tasks, modify the program to implement a random-walk motion for the particles: at each timestep the particle moves according to a uniform velocity motion, but after the move the velocity is changed randomly. 

OPTIONAL TASKS:
1. Modify the boundary conditions from hard reflective walls to periodic boundary conditions.


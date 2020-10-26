"""
Exam 1 Take-Home Project
The following is a program to simulate the motion of non-interacting particles inside a box
Time is discretized into small intervals (timesteps), during which the motion of the particles follow some simple physical laws
Trajectories of particles are simulated as a sequence of a large number of timesteps
 
Authors: O. Andreussi and STUDENT
"""
# TASK 4: This program should perform a simulation of a variable number of particle moving in two-dimensions inside a box with hard reflecting walls.
#         In this task you will modify the function to move particles so that their velocity changes randomly after each timestep. 
# 
# EXPECTED OUTCOME: An animation of a variable number of dots moving confusingly inside a rectangular box.
#
# Parameters and variables
# 
#    nparticles: number of particles in the simulation
#    dt: lenght of the timestep (in arbitrary units)
#    xbox: size of box along the x axis (in arbitrary units)
#    ybox: size of box along the y axis (in arbitrary units)
#    xpos: x component of particles positions (in arbitrary units)
#    ypos: y component of particles positions (in arbitrary units)
#    xvel: x component of particles velocities (in arbitrary units)
#    yvel: y component of particles velocities (in arbitrary units)
#
# Start by importing useful modules
#
import numpy as np
import matplotlib.animation as ani
import matplotlib.pyplot as plt
#
# Setup simulation parameters
# TASK4: to test your code you can choose a small number of particles (e.g. n=2) but your code should work for any integer number n > 0
#
nparticles= # TASK4: set this to an arbitrary number
dt=0.01 # this value should be reasonable, but you are free to test larger or smaller values
xbox=1. # when using arbitrary units is a good idea to keep them close to unity
ybox=1. # we start by considering a square box, but you are free to change this parameter as you like
#
# Setup starting configuration of the system
# TASK4: to test your code you can fix the initial positions and velocities by hand, but for a generic number of particles you want to 
# initialize positions and velocities using random numbers (e.g. using the numpy.random.uniform() function)
#
xpos=[] # TASK4: this should be a list (or a numpy array) with nparticles elements, corresponding to the x-coordinates of the particles. 
# NOTE: initial positions should be inside the [0,xbox] interval
ypos=[] # TASK4: this should be a list (or a numpy array) with nparticles elements, corresponding to the y-coordinates of the particles. 
# NOTE: initial positions should be inside the [0,ybox] interval. To test, you can start with values of zero for all the particles.
xvel=[] # TASK4: this should be a list (or a numpy array) with nparticles elements, corresponding to the x-component of the particles's velocities. 
# NOTE: initial velocities can be considered to be inside the [-1.,1.] interval.
yvel=[] # TASK4: this should be a list (or a numpy array) with nparticles elements, corresponding to the x-component of the particles's velocities. 
# NOTE: initial velocities can be considered to be inside the [-1.,1.] interval. To test, you can start with a constant value different from zero for all the particles. 
#
# The following is the function responsible to describe the motion of a single particle during a short timestep
#
def move(dt,xpos,ypos,xvel,yvel,xbox,ybox):
    """
    This function describes the motion of a single particle subject to no interactions but elastic reflections from the box walls.
    The particle's coordinates will change according to a constant velocity motion. 
    If the position of the particle falls outside of the box walls, the particle's velocity changes sign (reflection).
    Input arguments:
        dt: timestep; xpos/ypos: particle's coordinate along xy; xvel/yvel: x/y-component of particle's velocity; xbox/ybox: lenghts of box.
    Output results:
        updated x and y components of particle's position and velocity
    """
    # TAKS4: 
    #       1. write statements to update the particle's position (xpos and ypos) according to a 2D constant velocity motion
    #
    #       2. write statements to update the particle's velocity (xvel and yvel) drawing from the same random distribution used for initialization
    #
    #       3. write a conditional block to check if the new position falls within the intervals [0,xbox] and [0,ybox]. 
    #          If the new x and y components of the position are outside of their corresponding interval, 
    #          change them back to the position of the corresponding wall (0 or xbox/ybox).
    #       
    return xpos,ypos,xvel,yvel
#
# The following command setup the visualization of plot, where the particle is represented by a green filled circle
#
fig, axes = plt.subplots(1)
axes.set_xlim(0, xbox) # This statement set the limits for the x-axis of the plot
axes.set_ylim(0, ybox) # This statement set the limits for the y-axis of the plot.
a,=axes.plot(xpos,ypos,'go') # We generate a plot with the starting configuration
#
# Define the function that performs a single step of the animation
#
def animate(i):
    # Move each particle, one at a time
    for i in range(nparticles):
      xpos[i], ypos[i], xvel[i], yvel[i] = move(dt,xpos[i],ypos[i],xvel[i],yvel[i],xbox,ybox) # move particle i
    a.set_data(xpos,ypos) # update the plot
    return a,
#
# We perform the animation using the FuncAnimation function from the animation module of matplotlib. 
# This function requires as an argument the user-defined animate() function above
#
anim = ani.FuncAnimation(fig, animate, frames=1000, interval=50, blit=True)
#
# If you keep the following lines commented out, the code will only show the animation
# If you uncomment the following lines, the animation will be saved as an mp4 video
#
#Writer = ani.writers['ffmpeg']
#writer = Writer(fps=20, bitrate=1800)
#anim.save('task1.mp4', writer=writer)

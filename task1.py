"""
Exam 1 Take-Home Project

The following is a program to simulate the motion of non-interacting particles inside a box
Time is discretized into small intervals (timesteps), during which the motion of the particles follow some simple physical laws
Trajectories of particles are simulated as a sequence of a large number of timesteps
 
Authors: O. Andreussi and STUDENT
"""
# TASK 1: This program should perform a simulation of a single particle moving in one-dimension inside a box with hard reflecting walls.
#         This task only requires you to complete the move() function, but you can modify the parameters or the starting configuration
#         of the system to check the functioning of the program.
# 
# EXPECTED OUTCOME: An animation of a dot moving along the real axis and bounching back and forth inside the [0,1] interval.
#
# Parameters and variables
# 
#    nparticles: number of particles in the simulation
#    dt: lenght of the timestep (in arbitrary units)
#    xbox: size of box along the x axis (in arbitrary units)
#    xpos: x component of particles positions (in arbitrary units)
#    xvel: x component of particles velocities (in arbitrary units)
#
# Start by importing useful modules
#
import numpy as np
import matplotlib.animation as ani
import matplotlib.pyplot as plt
#
# Setup simulation parameters
#
nparticles=1 # for this assignment we only consider one particle 
dt=0.01 # this value should be reasonable, but you are free to test larger or smaller values
xbox=1. # when using arbitrary units is a good idea to keep them close to unity
#
# Setup starting configuration of the system
#
#
# Setup starting configuration of the system
#
xpos=0.0 # we start with the particle at the origin
xvel=1.0 # we start with some positive velocity along the x axis, but feel free to change and test different (positive or negative) values
#
# The following is the function responsible to describe the motion of a particle during a short timestep
#
def move(dt,xpos,xvel,xbox):
    """
    This function describes the motion of a particle subject to no interactions apart from elastic reflections from the box walls.
    The particle's coordinates will change according to a constant velocity motion. 
    If the position of the particle falls outside of the box walls, the particle's velocity changes sign (reflection).
    Input arguments:
        dt: timestep; xpos: particle's coordinate along x; xvel: x-component of particle's velocity; xbox: lenght of box.
    Output results:
        updated x-components of particle's position and velocity
    """
    # TAKS1: 
    #       1. write a statement to update the particle's position (xpos) according to a 1D constant velocity motion
    #
    #       2. write a conditional block to check if the new position falls within the interval [0,xbox]. 
    #          If the new position is outside of this interval, change the sign of the particle's velocity (xvel).
    #       
    return xpos, xvel
#
# The following command setup the visualization of plot, where the particle is represented by a green filled circle
#
fig, axes = plt.subplots(1)
axes.set_xlim(0, xbox) # This statement set the limits for the x-axis of the plot
axes.set_ylim(-0.01, 0.01) # This statement set the limits for the y-axis of the plot.
a,=axes.plot(xpos,0.,'go') # We generate a plot with the starting configuration
#
# Define the function that performs a single step of the animation
#
def animate(i):
    global xpos
    global xvel
    xpos, xvel = move(dt,xpos,xvel,xbox) # we move the particle
    a.set_data(xpos,0.) # we update the plot
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

"""
Exam 2 Take-Home Project

The following is a program to simulate the motion of objects interacting via gravitational forces. We will use the Velocity Verlet 
algorithm to integrate the equations of motion of the system's components.
 
Authors: O. Andreussi and STUDENT
"""
#
# Start by importing useful modules
#
import numpy as np
#
# Setup simulation parameters
#
dt= # TASK 4
maxtime = # TASK 4
#
# Setup starting configuration of the system 
# TASK 2
#
G = # TASK 2
#
# Earth
#
massE = # TASK 2
posE = [] # this should have at least two components TASK 2
velE =  [] # this should have at least two components TASK 2
#
# Sun (if you feel more comfortable, you can consider the Sun as not moving)
#
massS = # TASK 2
posS = [] # this should have at least two components TASK 2
velS = [] # this should have at least two components TASK 2
#
# Compute the forces acting on the system # TASK 1
#
def force(massA, posA, massB, posB):
    """
    This function computes the gravitational force acting on object A due to object B
    Input arguments:
        massA : the mass of object A
        posA: the position of object A
        massB : the mass of object B
        posB: the position of object B
    Output results:
        force: the force acting on object A (the one on B is going to be the opposite) 
        # NOTE the force should have the same number of components as the positions, so at least two
    """
    # TASK 1
    return force
#
# The following is the function responsible to describe the motion of a single particle during a short timestep
#
def move_position(dt,pos,vel,force,mass,box):
    """
    This function describes the motion of a single particle
    The particle's coordinates are updated according to Velocity Verlet algorithm. 
    Input arguments:
        dt: timestep; 
        pos: particle's coordinates; 
        vel: particle's velocity; 
        force: force acting on particle; 
        mass: mass of particle;
    Output results:
        pos: list with the updated positions of particles
    """
    for i in range(len(pos)):
       pos[i]=pos[i]+vel[i]*dt+0.5*force[i]/mass[i]*dt**2
    return pos
#
def move_velocity(dt,vel,forceold,forcenew,mass,box):
    """
    This function describes the motion of a single particle
    The particle's velocities are updated according to Velocity Verlet algorithm. 
    Input arguments:
        dt: timestep; 
        pos: particle's coordinates; 
        vel: particle's velocity; 
        forceold/forcenew: particle forces; 
        masses: mass of particle;
    Output results:
        vel: list with the updated velocity of the particle
    """
    for i in range(len(vel)):
       vel[i]=vel[i]+0.5*(forcenew[i]+forceold[i])/mass[i]*dt
    return vel
#
def kinetic_energy(mass,vel):
    """
    This functions computes the kinetic energy of a single object
    Input arguments:
        mass: mass of particle;
        vel: particle's velocity, at least 2 components;
    Output results:
        kinetic : kinetic energy of the system
    """
    kinetic = 0.0
    for i in range(len(vel)):
       kinetic = kinetic + 0.5 * mass * vel[i]**2
    return kinetic
#
def potential_energy(massA, posA, massB, posB): # TASK 1
    """
    This functions computes the gravitational potential energy of A interacting with B
    Input arguments:
        massA : the mass of object A
        posA: the position of object A
        massB : the mass of object B
        posB: the position of object B
    Output results:
        gravitational : gravitational energy of interaction of A and B
    """
    # TASK 1
    return gravitational
#
time=time0
r=[]
t=[]
forceEold=force() # YOU NEED TO ENTER THE APPROPRIATE ARGUMENTS
while time < maxtime : 
    t.append(time)
    r.append(pos.copy())
    time=time+dt
    # Update the Earth position
    posE=move_position(dt,posE,velE,forceEold,massE)
    # If you want you can update the Sun position
    #
    # Compute the new forces
    forceEnew=force() # YOU NEED TO ENTER THE APPROPRIATE ARGUMENTS
    # Update the Earth velocity
    velE=move_velocity(dt,velE,forceEold,forceEnew,massE)
    # If you want you can update the Sun velocity
    #
    # Save the forces for the next step
    forceEold=forceEnew
#
# TASK 3: Plot the kinetic, potential, and total energy of the projectile vs. time
#

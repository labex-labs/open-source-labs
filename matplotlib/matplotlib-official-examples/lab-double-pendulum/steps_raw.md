# Double Pendulum Simulation

## Introduction

The double pendulum is a classic problem in physics and mathematics. It involves two pendulums attached to each other, and the motion of the second pendulum is affected by the motion of the first pendulum. In this lab, we will use Python and Matplotlib to simulate the motion of a double pendulum.

## Steps

### Step 1: Import Required Libraries

We will begin by importing the necessary libraries for our simulation.

```python
from collections import deque
import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin
import matplotlib.animation as animation
```

### Step 2: Set Up Parameters

Next, we will define the parameters for our simulation. These parameters include the acceleration due to gravity, the length and mass of each pendulum, and the time interval for the simulation.

```python
G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
L = L1 + L2  # maximal length of the combined pendulum
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg
t_stop = 2.5  # how many seconds to simulate
history_len = 500  # how many trajectory points to display
```

### Step 3: Define the Derivatives Function

We will define a function that calculates the derivatives of the system at any given time. This function takes in the current state of the system (the angles and angular velocities of each pendulum) and returns the derivatives of those values.

```python
def derivs(t, state):
    dydx = np.zeros_like(state)

    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)

    return dydx
```

### Step 4: Set Up Initial Conditions and Integrate the ODE

We will now set up the initial conditions for our simulation. We will set the initial angles and angular velocities of each pendulum, as well as the time interval for the simulation. We will then integrate the ODE using Euler's method to get the position and velocity of each pendulum at each time step.

```python
# create a time array from 0..t_stop sampled at 0.02 second steps
dt = 0.01
t = np.arange(0, t_stop, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# integrate the ODE using Euler's method
y = np.empty((len(t), 4))
y[0] = state
for i in range(1, len(t)):
    y[i] = y[i - 1] + derivs(t[i - 1], y[i - 1]) * dt
```

### Step 5: Calculate the Position of Each Pendulum

We will now use the position and velocity of each pendulum at each time step to calculate the x and y coordinates of each pendulum.

```python
x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1
```

### Step 6: Set Up the Plot

We will now set up the plot for our simulation. We will create a figure with an x and y limit equal to the maximum length of the pendulum, set the aspect ratio to be equal, and add a grid.

```python
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, 1.))
ax.set_aspect('equal')
ax.grid()
```

### Step 7: Define the Animation Function

We will define a function that will animate the motion of the double pendulum. This function will take in the current time step and use it to update the position of each pendulum. It will also update the trajectory of the second pendulum.

```python
line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], '.-', lw=1, ms=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
history_x, history_y = deque(maxlen=history_len), deque(maxlen=history_len)

def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    if i == 0:
        history_x.clear()
        history_y.clear()

    history_x.appendleft(thisx[2])
    history_y.appendleft(thisy[2])

    line.set_data(thisx, thisy)
    trace.set_data(history_x, history_y)
    time_text.set_text(time_template % (i*dt))
    return line, trace, time_text
```

### Step 8: Create the Animation

We will now create the animation using the FuncAnimation function from Matplotlib.

```python
ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
```

## Summary

In this lab, we used Python and Matplotlib to simulate the motion of a double pendulum. We set up the parameters for our simulation, defined a function to calculate the derivatives of the system, integrated the ODE using Euler's method, calculated the position of each pendulum at each time step, and created an animation of the motion of the double pendulum.

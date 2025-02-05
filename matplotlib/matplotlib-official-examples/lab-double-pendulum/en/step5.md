# Calculate the Position of Each Pendulum

We will now use the position and velocity of each pendulum at each time step to calculate the x and y coordinates of each pendulum.

```python
x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1
```

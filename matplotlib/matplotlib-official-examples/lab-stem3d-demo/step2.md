# Define the data

In this step, we will define the data that we will use to create the 3D stem plot. We will create a linspace array for the angle, and use sine and cosine functions to calculate the x and y coordinates. We will also define the z coordinate as the angle.

```python
theta = np.linspace(0, 2*np.pi)
x = np.cos(theta - np.pi/2)
y = np.sin(theta - np.pi/2)
z = theta
```

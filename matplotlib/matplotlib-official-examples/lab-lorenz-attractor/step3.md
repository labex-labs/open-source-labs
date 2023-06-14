# Set Up the Initial Parameters

We set up the initial parameters for the simulation, including the time step `dt`, the number of steps `num_steps`, and the initial values for `x`, `y`, and `z`.

```python
dt = 0.01
num_steps = 10000

xyzs = np.empty((num_steps + 1, 3))  # Need one more for the initial values
xyzs[0] = (0., 1., 1.05)  # Set initial values
```

# Calculate the Lorenz Attractor

We calculate the Lorenz Attractor by stepping through time and estimating the next point using the previous point and the Lorenz function.

```python
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt
```

# Create the 3D stem plot

In this step, we will create the 3D stem plot using the `stem` function from Matplotlib. We will pass the x, y, and z coordinates as arguments to the `stem` function.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

plt.show()
```

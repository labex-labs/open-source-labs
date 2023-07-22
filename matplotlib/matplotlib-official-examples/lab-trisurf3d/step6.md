# Create the 3D Surface

We will create the 3D surface using the `plot_trisurf` function:

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()
```

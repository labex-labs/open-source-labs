# Create the Figure and Subplots

We will create a figure with two subplots. The first subplot will be a 3D surface plot, and the second subplot will be a 3D wireframe plot.

```python
# Create a figure with two subplots
fig = plt.figure(figsize=plt.figaspect(0.5))

# Add the first subplot with 3D projection
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# Add the second subplot with 3D projection
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
```

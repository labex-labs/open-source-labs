# Create the Plot

We will now create the plot using Matplotlib by adding two `PathPatch` objects to the plot. One will be an orange filled shape, while the other will be a white outline.

```python
# Set the plot limits
xmin, ymin = verts.min(axis=0) - 1
xmax, ymax = verts.max(axis=0) + 1

# Create the plot
fig = plt.figure(figsize=(5, 5), facecolor="0.75")  # gray background
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1,
                  xlim=(xmin, xmax),  # centering
                  ylim=(ymax, ymin),  # centering, upside down
                  xticks=[], yticks=[])  # no ticks

# Add the white outline
ax.add_patch(patches.PathPatch(path, facecolor='none', edgecolor='w', lw=6))

# Add the orange shape
ax.add_patch(patches.PathPatch(path, facecolor='orange', edgecolor='k', lw=2))

# Display the plot
plt.show()
```

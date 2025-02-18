# Tracer des ellipses individuelles

Dans cet exemple, nous allons tracer de nombreuses ellipses avec des tailles, des positions et des couleurs aléatoires. Chaque ellipse sera une instance de la classe `Ellipse`.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Number of ellipses to draw
NUM = 250

# Generate the ellipses
ells = [Ellipse(xy=np.random.rand(2) * 10,
                width=np.random.rand(), height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

# Create the plot and set the aspect ratio to 'equal'
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# Add each ellipse to the plot
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
    e.set_facecolor(np.random.rand(3))

# Set the x and y limits of the plot
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Show the plot
plt.show()
```

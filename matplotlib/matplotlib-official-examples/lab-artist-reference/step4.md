# Customize Shapes

We can customize the shapes by setting various properties such as color, edge color, and alpha.

```python
shapes = [
    mpatches.Circle((0, 0), 0.1, color='red', alpha=0.5),
    mpatches.Rectangle((-0.025, -0.05), 0.05, 0.1, ec="none", color='green', alpha=0.5),
    mpatches.Wedge((0, 0), 0.1, 30, 270, ec="none", color='blue', alpha=0.5),
    mpatches.RegularPolygon((0, 0), 5, radius=0.1, color='orange', alpha=0.5),
    mpatches.Ellipse((0, 0), 0.2, 0.1, color='purple', alpha=0.5),
    mpatches.Arrow(-0.05, -0.05, 0.1, 0.1, width=0.1, color='yellow', alpha=0.5),
    mpatches.PathPatch(mpath.Path([(0, 0), (0.5, 0.5), (1, 0)], [1, 2, 2]), ec="none", color='pink', alpha=0.5),
    mpatches.FancyBboxPatch((-0.025, -0.05), 0.05, 0.1, ec="none", color='brown', alpha=0.5,
                            boxstyle=mpatches.BoxStyle("Round", pad=0.02)),
]

fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.show()
```

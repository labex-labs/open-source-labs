# Plot a Curved Line with Ticked Patheffect

We will now plot a curved line with ticked patheffect.

```python
# Plot a curved line with ticked style path
ax.plot(x, y, label="Curve", path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
```

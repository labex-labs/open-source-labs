# Plot a Straight Line with Ticked Patheffect

We will now plot a straight diagonal line with ticked patheffect.

```python
# Plot a straight diagonal line with ticked style path
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0, 1], [0, 1], label="Line",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])
```

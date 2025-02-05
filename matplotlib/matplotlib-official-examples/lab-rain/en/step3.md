# Construct the Scatter Plot

Now, we will construct the scatter plot which we will update during the animation as the raindrops develop.

```python
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors='none')
```

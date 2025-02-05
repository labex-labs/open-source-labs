# Shade the Regions

We will use `fill_between` to shade the regions above and below the horizontal line where the sine wave is positive and negative, respectively.

```python
ax.fill_between(t, 1, where=s > 0, facecolor='green', alpha=.5)
ax.fill_between(t, -1, where=s < 0, facecolor='red', alpha=.5)
```

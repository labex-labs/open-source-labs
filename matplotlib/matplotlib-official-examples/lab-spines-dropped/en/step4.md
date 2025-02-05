# Offset the Spines

We will move the left and bottom spines outward by 10 points using the `set_position()` function. The argument for `set_position()` is a tuple with two elements. The first element represents the position of the spine, and the second element represents the distance from the spine to the plot area.

```python
ax.spines[['left', 'bottom']].set_position(('outward', 10))
```

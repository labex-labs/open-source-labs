# Reverse the Orientation Arrow

If you want to reverse the orientation arrow, you can switch the marker type from `>` to `<`.

```python
# To reverse the orientation arrow, switch the marker type from > to <.
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle("<", "full", t),
    markersize=10
)
```

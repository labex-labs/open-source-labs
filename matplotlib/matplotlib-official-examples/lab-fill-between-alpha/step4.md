# Highlighting Spans of an Axes with `axhspan` and `axvspan`

Another handy use of filled regions is to highlight horizontal or vertical spans of an Axes. For that Matplotlib has the helper functions `axhspan` and `axvspan`. See the `axhspan_demo` gallery for more information.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)
ax.axvspan(6, 7, facecolor='r', alpha=0.5)

plt.show()
```

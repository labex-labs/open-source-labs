# Add lines to the Figure

We can add lines to the figure using the `fig.add_artist()` method. We will create two lines - one from (0,0) to (1,1) and another from (0,1) to (1,0).

```python
fig.add_artist(lines.Line2D([0, 1], [0, 1]))
fig.add_artist(lines.Line2D([0, 1], [1, 0]))
```

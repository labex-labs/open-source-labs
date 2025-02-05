# Add text annotations to the plot

Next, we'll add text annotations to the plot using the `ax.text()` function. We'll create two annotations, one for "Sample A" and one for "Sample B".

```python
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.text(-2, -2, "Sample A", ha="center", va="center", size=20,
        bbox=bbox_props)
ax.text(2, 2, "Sample B", ha="center", va="center", size=20,
        bbox=bbox_props)
```

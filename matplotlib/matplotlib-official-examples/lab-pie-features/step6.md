# Customize the Hatch Patterns

We can customize the hatch patterns of the slices by passing a list of hatch patterns to the `hatch` parameter of the `pie()` function.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, hatch=['**O', 'oO', 'O.O', '.||.'])
```

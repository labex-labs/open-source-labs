# Hide unnecessary spines

You also want to hide the top and right spines since they are not needed.

```python
ax.spines[["top", "right"]].set_visible(False)
```

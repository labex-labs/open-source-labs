# Draw arrows at the end of the spines

To indicate the direction of the axes, you can draw arrows at the end of the spines.

```python
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
```

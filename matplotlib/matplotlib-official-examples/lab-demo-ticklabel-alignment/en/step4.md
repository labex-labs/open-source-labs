# Adjust Tick Label Alignment

Finally, we can use the `set_ha` and `set_va` methods to adjust the horizontal and vertical alignment of tick labels.

```python
ax.axis["left"].major_ticklabels.set_ha("center")
ax.axis["bottom"].major_ticklabels.set_va("top")
```

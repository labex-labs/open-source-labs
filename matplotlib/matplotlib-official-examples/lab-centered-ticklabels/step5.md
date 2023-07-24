# Align the Minor Tick Labels

Finally, we need to align the minor tick labels to the center between the major ticks. We can do this using the `get_xticklabels()` function and setting the `minor` parameter to `True` to get the minor tick labels. We can then loop through the labels and set the horizontal alignment to `'center'`.

```python
# Align the minor tick label
for label in ax.get_xticklabels(minor=True):
    label.set_horizontalalignment('center')
imid = len(r) // 2
ax.set_xlabel(str(r.date[imid].item().year))
```

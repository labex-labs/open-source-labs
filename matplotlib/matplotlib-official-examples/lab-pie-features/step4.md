# Add Labels to the Slices

We can add labels to the slices by passing a list of labels to the `labels` parameter of the `pie()` function.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
```

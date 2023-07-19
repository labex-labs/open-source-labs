# Top Title

Create a plot with the title at the top using the `subplots()` function and the `set_xlabel()` function.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Top Title')
```

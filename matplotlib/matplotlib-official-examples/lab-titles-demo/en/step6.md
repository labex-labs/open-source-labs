# Manual Y Positioning

Manually specify the vertical position of the title by using the `y` parameter of the `title()` function.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Manual Y Positioning', y=1.0)
```

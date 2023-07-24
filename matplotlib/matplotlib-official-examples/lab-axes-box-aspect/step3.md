# Square Twin Axes

We will produce a square axes, with a twin axes. The twinned axes takes over the box aspect of the parent.

```python
fig3, ax = plt.subplots()

ax2 = ax.twinx()

ax.plot([0, 10])
ax2.plot([12, 10])

ax.set_box_aspect(1)

plt.show()
```

# データ空間で固定された全体のパッチ

```python
fig, axs = plt.subplots(nrows=2)

arrow = mpatches.Arrow(x_tail, y_tail, dx, dy)
axs[0].add_patch(arrow)

arrow = mpatches.FancyArrow(x_tail, y_tail -.4, dx, dy,
                            width=.1, length_includes_head=True, color="C1")
axs[0].add_patch(arrow)

axs[0].arrow(x_tail + 1, y_tail -.4, dx, dy,
             width=.1, length_includes_head=True, color="C2")

arrow = mpatches.Arrow(x_tail, y_tail, dx, dy)
axs[1].add_patch(arrow)

arrow = mpatches.FancyArrow(x_tail, y_tail -.4, dx, dy,
                            width=.1, length_includes_head=True, color="C1")
axs[1].add_patch(arrow)

axs[1].arrow(x_tail + 1, y_tail -.4, dx, dy,
             width=.1, length_includes_head=True, color="C2")
axs[1].set(xlim=(0, 2), ylim=(0, 2))

plt.show()
```

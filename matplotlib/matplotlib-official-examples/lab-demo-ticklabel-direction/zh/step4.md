# 刻度标签向外指向

在这一步中，我们将创建一个子图，其中刻度标签向外指向。

```python
fig = plt.figure(figsize=(6, 3))
fig.subplots_adjust(bottom=0.2)

ax = setup_axes(fig, 131)
for axis in ax.axis.values():
    axis.major_ticks.set_tick_out(True)
```

# 手动对齐 y 轴标签

第四步是使用 y 轴对象的`~.Axis.set_label_coords`方法手动对齐 y 轴标签。

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)

labex = -0.3  # axes coords

for j in range(2):
    axs[j, 1].yaxis.set_label_coords(labex, 0.5)

plt.show()
```

# 自动对齐y轴标签

第三步是使用`.Figure.align_ylabels`方法自动对齐y轴标签。

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)
fig.align_ylabels(axs[:, 1])
plt.show()
```

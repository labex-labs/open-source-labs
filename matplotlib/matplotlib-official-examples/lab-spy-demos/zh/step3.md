# 创建子图

现在我们将使用`subplots`函数创建一个2x2的子图网格。这将为我们提供四个图来可视化数组的稀疏模式。

```python
fig, axs = plt.subplots(2, 2)
ax1 = axs[0, 0]
ax2 = axs[0, 1]
ax3 = axs[1, 0]
ax4 = axs[1, 1]
```

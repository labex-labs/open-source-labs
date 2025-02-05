# 为图形添加标签

在这一步中，我们将为图形添加标签。我们会添加一个标题、网格线以及x轴和y轴的标签。

```python
fig.suptitle("累积分布")
for ax in axs:
    ax.grid(True)
    ax.legend()
    ax.set_xlabel("年降雨量 (毫米)")
    ax.set_ylabel("发生概率")
    ax.label_outer()

plt.show()
```

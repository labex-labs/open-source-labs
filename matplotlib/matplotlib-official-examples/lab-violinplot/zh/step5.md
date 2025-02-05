# 自定义图表外观

我们将通过移除 y 轴标签并为图表添加标题来自定义图表的外观。

```python
for ax in axs.flat:
    ax.set_yticklabels([])

fig.suptitle("Violin Plotting Examples")
fig.subplots_adjust(hspace=0.4)
plt.show()
```

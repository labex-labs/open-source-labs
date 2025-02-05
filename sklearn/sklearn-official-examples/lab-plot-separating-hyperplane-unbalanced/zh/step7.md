# 添加图例

我们将使用 `matplotlib.pyplot` 中的 `legend` 函数为图表添加图例。我们将分别把标签设置为 “未加权” 和 “加权”。

```python
plt.legend(
    [disp.surface_.collections[0], wdisp.surface_.collections[0]],
    ["non weighted", "weighted"],
    loc="upper right",
)
```

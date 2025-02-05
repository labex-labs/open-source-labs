# 添加图例

要为我们的图表添加图例，我们使用 Matplotlib 的 `legend` 函数。我们传入 `loc` 参数来指定图例的位置，传入 `shadow` 参数为图例添加阴影效果。我们还使用 `fontsize` 参数来设置图例的字体大小。

```python
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
```

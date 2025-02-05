# 添加颜色条

使用 `colorbar` 方法添加颜色条。我们将设置 `fraction` 和 `pad` 参数来调整颜色条的位置，并设置标签以显示数据的名称和单位。

```python
# 颜色条
fig.colorbar(C, ax=ax, fraction=0.02, pad=0.1, label='Name [units]')
```

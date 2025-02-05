# 自定义 Z 轴

```python
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
```

我们使用 `set_zlim()` 函数自定义 z 轴，将 z 轴的范围设置为 -1.01 到 1.01。然后，我们使用 `set_major_locator()` 函数，通过 `LinearLocator(10)` 将 z 轴上的刻度数量设置为 10。最后，我们使用 `set_major_formatter()` 函数，通过 `StrMethodFormatter` 来格式化 z 轴刻度标签。

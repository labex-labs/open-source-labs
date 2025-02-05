# 关闭刻度标签

要从每个内嵌图中移除刻度标签，我们可以使用 `tick_params()` 方法，并将 `labelleft` 和 `labelbottom` 设置为 `False`。

```python
# 关闭内嵌图的刻度标签
for axi in [axins, axins2, axins3, axins4]:
    axi.tick_params(labelleft=False, labelbottom=False)
```

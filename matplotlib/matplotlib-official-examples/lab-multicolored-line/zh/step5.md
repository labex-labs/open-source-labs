# 创建一个颜色条

我们将创建一个颜色条来展示颜色与 `dydx` 值之间的映射关系。我们会使用 `matplotlib.pyplot` 中的 `colorbar` 函数来创建一个颜色条。

```python
line = plt.gca().add_collection(lc)
plt.colorbar(line)
```

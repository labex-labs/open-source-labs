# 添加上限

要给误差线添加上限，我们将使用`errorbar`函数的`uplims`参数。我们还将给 y 值加上一个常数 0.5，以便将此图与前一个图区分开来。

```python
# 包括上限
ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=True, linestyle='dotted')
```

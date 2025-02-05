# 添加上限和下限

要给误差线同时添加上限和下限，我们将使用`errorbar`函数的`uplims`和`lolims`参数。我们还将在图中添加一个标记，以便将其与之前的图区分开来。

```python
# 包括上限和下限
ax.errorbar(x, y + 1.5, xerr=xerr, yerr=yerr, lolims=True, uplims=True,
            marker='o', markersize=8, linestyle='dotted')
```

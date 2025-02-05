# 添加下限

要给误差线添加下限，我们将使用`errorbar`函数的`lolims`参数。我们还将给y值加上一个常数1.0，以便将此图与之前的图区分开来。

```python
# 包括下限
ax.errorbar(x, y + 1.0, xerr=xerr, yerr=yerr, lolims=True, linestyle='dotted')
```

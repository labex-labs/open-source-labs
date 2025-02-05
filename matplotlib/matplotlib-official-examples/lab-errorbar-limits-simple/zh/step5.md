# 创建带有上下限的误差线图

在这一步中，我们创建一个带有上限和下限的误差线图。

```python
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True, label='uplims=True, lolims=True')
```

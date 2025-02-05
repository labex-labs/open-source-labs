# 创建仅带有上限的误差线图

在这一步中，我们创建一个仅带有上限的误差线图。

```python
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
```

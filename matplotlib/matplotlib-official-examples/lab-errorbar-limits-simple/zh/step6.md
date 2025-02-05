# 创建带有上下限子集的误差线图

在这一步中，我们创建一个带有上下限子集的误差线图。

```python
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits, label='subsets of uplims and lolims')
```

# 创建幂律归一化

在这一步中，你需要使用 `PowerNorm()` 创建幂律归一化。

```python
plt.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```

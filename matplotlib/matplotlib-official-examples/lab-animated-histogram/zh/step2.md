# 设置随机种子和 bins

设置随机种子以确保可重复性，并确定 bins 的边界。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Fixing bin edges
HIST_BINS = np.linspace(-4, 4, 100)
```

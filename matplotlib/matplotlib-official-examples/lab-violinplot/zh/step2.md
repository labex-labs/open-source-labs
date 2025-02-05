# 创建示例数据集

我们将使用 numpy 库创建一个示例数据集。我们将创建六个具有不同标准差的数据集。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# fake data
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]
```

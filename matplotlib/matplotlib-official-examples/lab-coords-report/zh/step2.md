# 创建数据

接下来，我们将创建一些随机数据用于可视化。在本示例中，我们将使用 numpy 创建两个随机数据数组。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.random.rand(20)
y = 1e7 * np.random.rand(20)
```

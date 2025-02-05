# 创建人工数据

我们需要创建一些用于绘图的人工数据。在本实验中，我们将绘制频率（单位：赫兹）的对数与功率（单位：瓦特）的对数的关系图。我们将使用 `numpy` 库来生成数据。

```python
# Fixing random state for reproducibility
prng = np.random.RandomState(19680801)

# Create artificial data to plot.
# The x data span over several decades to demonstrate several SI prefixes.
xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * prng.uniform(size=100)) * np.log10(xs)**2
```

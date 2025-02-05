# 创建降雨数据

接下来，我们将创建降雨数据。我们将在随机位置创建 50 个雨滴，每个雨滴具有随机的增长速度和随机颜色。

```python
n_drops = 50
rain_drops = np.zeros(n_drops, dtype=[('position', float, (2,)),
                                      ('size',     float),
                                      ('growth',   float),
                                      ('color',    float, (4,))])

rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)
```

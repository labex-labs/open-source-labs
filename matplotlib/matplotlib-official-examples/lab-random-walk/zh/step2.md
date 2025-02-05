# 定义随机游走函数

我们定义一个函数，该函数生成具有给定步数和最大步长的随机游走。该函数有两个输入：`num_steps` 是随机游走中的总步数，`max_step` 是每一步的最大步长。我们使用 `numpy.random` 生成步长的随机数，并使用 `numpy.cumsum` 计算步长的累积和以获得最终位置。

```python
def random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array."""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk
```

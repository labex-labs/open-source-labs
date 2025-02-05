# 创建更新函数

更新函数将由 `FuncAnimation` 对象调用，以便在动画过程中更新散点图。

```python
def update(frame_number):
    # 获取一个索引，用于重新生成最老的雨滴。
    current_index = frame_number % n_drops

    # 随着时间推移，使所有颜色变得更透明。
    rain_drops['color'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

    # 使所有圆圈变大。
    rain_drops['size'] += rain_drops['growth']

    # 为最老的雨滴选择一个新位置，重置其大小、颜色和增长因子。
    rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)
    rain_drops['size'][current_index] = 5
    rain_drops['color'][current_index] = (0, 0, 0, 1)
    rain_drops['growth'][current_index] = np.random.uniform(50, 200)

    # 使用新的颜色、大小和位置更新散点集合。
    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
```

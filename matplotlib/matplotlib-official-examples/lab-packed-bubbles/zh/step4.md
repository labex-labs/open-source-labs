# 定义气泡移动方法

`BubbleChart` 类还包含将气泡移向质心以及检查与其他气泡碰撞的方法。`center_of_mass` 方法计算所有气泡的质心，`center_distance` 方法计算一个气泡与质心之间的距离。`outline_distance` 方法计算一个气泡的轮廓与其他气泡轮廓之间的距离，`check_collisions` 方法检查新的气泡位置是否与其他气泡发生碰撞。

```python
    def center_of_mass(self):
        return np.average(
            self.bubbles[:, :2], axis=0, weights=self.bubbles[:, 3]
        )

    def center_distance(self, bubble, bubbles):
        return np.hypot(bubble[0] - bubbles[:, 0],
                        bubble[1] - bubbles[:, 1])

    def outline_distance(self, bubble, bubbles):
        center_distance = self.center_distance(bubble, bubbles)
        return center_distance - bubble[2] - \
            bubbles[:, 2] - self.bubble_spacing

    def check_collisions(self, bubble, bubbles):
        distance = self.outline_distance(bubble, bubbles)
        return len(distance[distance < 0])
```

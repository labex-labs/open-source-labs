# バブルの移動方法を定義する

`BubbleChart` クラスには、バブルを質量中心に向かって移動させ、他のバブルとの衝突をチェックするメソッドも含まれています。`center_of_mass` メソッドは、すべてのバブルの質量中心を計算し、`center_distance` メソッドは、バブルと質量中心との距離を計算します。`outline_distance` メソッドは、バブルの輪郭と他のバブルの輪郭との距離を計算し、`check_collisions` メソッドは、新しいバブルの位置が他のバブルと衝突するかどうかをチェックします。

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

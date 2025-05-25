# 버블 이동 메서드 정의

`BubbleChart` 클래스는 또한 버블을 질량 중심 (center of mass) 으로 이동하고 다른 버블과의 충돌을 확인하는 메서드를 포함합니다. `center_of_mass` 메서드는 모든 버블의 질량 중심을 계산하고, `center_distance` 메서드는 버블과 질량 중심 사이의 거리를 계산합니다. `outline_distance` 메서드는 버블의 외곽선과 다른 버블의 외곽선 사이의 거리를 계산하고, `check_collisions` 메서드는 새로운 버블 위치가 다른 버블과 충돌하는지 확인합니다.

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

# Определяем методы движения пузырьков

Класс `BubbleChart` также содержит методы для перемещения пузырьков к центру масс и проверки на столкновения с другими пузырьками. Метод `center_of_mass` вычисляет центр масс всех пузырьков, а метод `center_distance` вычисляет расстояние между пузырьком и центром масс. Метод `outline_distance` вычисляет расстояние между контурами пузырька и контурами других пузырьков, а метод `check_collisions` проверяет, сталкивается ли новая позиция пузырька с другими пузырьками.

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

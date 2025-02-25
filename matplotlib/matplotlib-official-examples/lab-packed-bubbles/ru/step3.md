# Определяем класс BubbleChart

Класс `BubbleChart` используется для создания графика с упакованными пузырьками. Класс принимает массив площадей пузырьков и значение расстояния между пузырьками. Метод `__init__` настраивает начальные позиции пузырьков и вычисляет максимальное расстояние шага, которое представляет собой расстояние, на которое каждый пузырек может переместиться за одну итерацию.

```python
class BubbleChart:
    def __init__(self, area, bubble_spacing=0):
        """
        Настройка для сжатия пузырьков.

        Параметры
        ----------
        area : array-like
            Площадь пузырьков.
        bubble_spacing : float, по умолчанию: 0
            Минимальное расстояние между пузырьками после сжатия.

        Примечания
        -----
        Если "area" отсортирован, результаты могут выглядеть странно.
        """
        area = np.asarray(area)
        r = np.sqrt(area / np.pi)

        self.bubble_spacing = bubble_spacing
        self.bubbles = np.ones((len(area), 4))
        self.bubbles[:, 2] = r
        self.bubbles[:, 3] = area
        self.maxstep = 2 * self.bubbles[:, 2].max() + self.bubble_spacing
        self.step_dist = self.maxstep / 2

        # вычисляем начальную сеточную разметку для пузырьков
        length = np.ceil(np.sqrt(len(self.bubbles)))
        grid = np.arange(length) * self.maxstep
        gx, gy = np.meshgrid(grid, grid)
        self.bubbles[:, 0] = gx.flatten()[:len(self.bubbles)]
        self.bubbles[:, 1] = gy.flatten()[:len(self.bubbles)]

        self.com = self.center_of_mass()
```

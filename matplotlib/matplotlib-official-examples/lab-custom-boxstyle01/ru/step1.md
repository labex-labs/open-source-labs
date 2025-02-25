# Реализация пользовательского стиля рамки в виде функции

Пользовательские стили рамок можно реализовать в виде функций, которые принимают аргументы, определяющие как прямоугольную рамку, так и количество «мьютации», и возвращают «измененную» траекторию. Здесь мы реализуем пользовательский стиль рамки, который возвращает новую траекторию, которая добавляет на левую сторону рамки форму «стрелки».

```python
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
from matplotlib.path import Path

def custom_box_style(x0, y0, width, height, mutation_size):
    """
    Данное расположение и размер рамки, возвращает траекторию рамки вокруг нее.

    Поворот автоматически обрабатывается.

    Параметры
    ----------
    x0, y0, width, height : float
        Расположение и размер рамки.
    mutation_size : float
        Ссылка на масштаб мьютации, обычно размер шрифта текста.
    """
    # отступ
    mypad = 0.3
    pad = mutation_size * mypad
    # ширина и высота с добавленным отступом.
    width = width + 2 * pad
    height = height + 2 * pad
    # граница отступленной рамки
    x0, y0 = x0 - pad, y0 - pad
    x1, y1 = x0 + width, y0 + height
    # возвращаем новую траекторию
    return Path([(x0, y0),
                 (x1, y0), (x1, y1), (x0, y1),
                 (x0-pad, (y0+y1)/2), (x0, y0),
                 (x0, y0)],
                closed=True)

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle=custom_box_style, alpha=0.2))
plt.show()
```

# Импортируем библиотеки и определяем функцию

Первым шагом является импорт необходимых библиотек и определение функции `make_arrow_graph()`. Эта функция принимает различные параметры, такие как оси, данные, размер, отображение, форма, максимальная ширина стрелки, расстояние между стрелками, альфа, нормализация данных, цвет контура, цвет метки и дополнительные именованные аргументы. Она использует эти параметры для создания диаграммы с стрелками.

```python
# Import libraries
import itertools
import matplotlib.pyplot as plt
import numpy as np

# Define the function
def make_arrow_graph(ax, data, size=4, display='length', shape='right',
                     max_arrow_width=0.03, arrow_sep=0.02, alpha=0.5,
                     normalize_data=False, ec=None, labelcolor=None,
                     **kwargs):
    """
    Создает диаграмму с стрелками.

    Параметры
    ----------
    ax
        Оси, на которых рисуется график.
    data
        Словарь с вероятностями для оснований и переходов пар.
    size
        Размер графика в дюймах.
    display : {'length', 'width', 'alpha'}
        Свойство стрелки, которое меняется.
    shape : {'full', 'left', 'right'}
        Для полных или полустрелок.
    max_arrow_width : float
        Максимальная ширина стрелки в координатах данных.
    arrow_sep : float
        Расстояние между стрелками в паре в координатах данных.
    alpha : float
        Максимальная прозрачность стрелок.
    **kwargs
        Свойства `.FancyArrow`, например *linewidth* или *edgecolor*.
    """

    # code block
```

# Определяем линии контура и полигоны

Следующим шагом является определение линий контура и полигонов. В этом примере у нас есть линии и заполненные контура между двумя уровнями.

```python
# Линии контура для каждого уровня представляют собой список/кортеж полигонов.
lines0 = [[[0, 0], [0, 4]]]
lines1 = [[[2, 0], [1, 2], [1, 3]]]
lines2 = [[[3, 0], [3, 2]], [[3, 3], [3, 4]]]  # Обратите внимание на две линии.

# Заполненные контура между двумя уровнями также представляют собой список/кортеж полигонов.
# Точки могут быть упорядочены по часовой стрелке или против часовой стрелки.
filled01 = [[[0, 0], [0, 4], [1, 3], [1, 2], [2, 0]]]
filled12 = [[[2, 0], [3, 0], [3, 2], [1, 3], [1, 2]],   # Обратите внимание на два полигона.
            [[1, 4], [3, 4], [3, 3]]]
```

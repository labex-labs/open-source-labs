# Определяем макет трехмерной диаграммы

Определяем макет трехмерной диаграммы с использованием списка списков. Точка `'.'` в списке представляет собой пустой подграфик.

```python
layout = [['XY',  '.',   'L',   '.'],
          ['XZ', 'YZ', '-XZ', '-YZ'],
          ['.',   '.', '-XY',   '.']]
```

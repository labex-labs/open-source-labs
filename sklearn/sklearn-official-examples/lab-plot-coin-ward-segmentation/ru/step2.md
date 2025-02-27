# Определение структуры данных

Пиксели на изображении соединены с их соседями. Чтобы выполнить иерархическую кластеризацию на изображении, нам нужно определить структуру данных. Мы можем использовать функцию `grid_to_graph` из scikit-learn для создания матрицы связности, которая определяет структуру данных.

```python
from sklearn.feature_extraction.image import grid_to_graph

connectivity = grid_to_graph(*rescaled_coins.shape)
```

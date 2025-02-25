# Импортируем Matplotlib и создаем точечный график

Начнем с импорта Matplotlib и создания точечного графика.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sc = ax.scatter([1, 2], [1, 2], c=[1, 2])
```

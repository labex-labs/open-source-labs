# Импортируем Matplotlib и создаем фигуру и оси

Сначала вам нужно импортировать Matplotlib и создать фигуру и оси. Фигура и оси - это контейнеры для вашего графика.

```python
import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
```

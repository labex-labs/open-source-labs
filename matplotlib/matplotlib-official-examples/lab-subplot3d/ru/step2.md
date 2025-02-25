# Создаем фигуру и подграфики

Мы создадим фигуру с двумя подграфиками. Первый подграфик будет трехмерной поверхностной диаграммой, а второй подграфик будет трехмерной линейной диаграммой.

```python
# Create a figure with two subplots
fig = plt.figure(figsize=plt.figaspect(0.5))

# Add the first subplot with 3D projection
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# Add the second subplot with 3D projection
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
```

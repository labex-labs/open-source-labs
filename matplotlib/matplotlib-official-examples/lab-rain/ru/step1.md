# Создание новой фигуры и осей

Первым шагом является создание новой фигуры и осей, которые заполняют ее. Это будет холст, на котором будет нарисована симуляция.

```python
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
```

# Создаем и визуализируем графики частичной зависимости

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, grid_resolution=20)

# Задаем размеры рисунка и заголовок
fig.set_size_inches(10, 8)
fig.suptitle('Графики частичной зависимости')

plt.show()
```

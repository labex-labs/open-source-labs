# Создаем и визуализируем графики индивидуального условного ожидания

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, kind='individual')

# Задаем размеры рисунка и заголовок
fig.set_size_inches(10, 8)
fig.suptitle('Графики индивидуального условного ожидания')

plt.show()
```

# Crear y visualizar gráficas de expectativa condicional individual

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, kind='individual')

# Establecer el tamaño de la figura y el título
fig.set_size_inches(10, 8)
fig.suptitle('Gráficas de Expectativa Condicional Individual')

plt.show()
```

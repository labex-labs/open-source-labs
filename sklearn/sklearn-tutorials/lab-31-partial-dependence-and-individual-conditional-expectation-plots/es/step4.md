# Crear y visualizar gráficas de dependencia parcial

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, grid_resolution=20)

# Establecer el tamaño de la figura y el título
fig.set_size_inches(10, 8)
fig.suptitle('Gráficas de Dependencia Parcial')

plt.show()
```

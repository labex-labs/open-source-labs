# Criar e visualizar gráficos de dependência parcial

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, grid_resolution=20)

# Definir o tamanho da figura e o título
fig.set_size_inches(10, 8)
fig.suptitle('Gráficos de Dependência Parcial')

plt.show()
```

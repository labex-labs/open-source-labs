# Criar e visualizar gráficos de expectativa condicional individual

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, kind='individual')

# Definir o tamanho da figura e o título
fig.set_size_inches(10, 8)
fig.suptitle('Gráficos de Expectativa Condicional Individual')

plt.show()
```

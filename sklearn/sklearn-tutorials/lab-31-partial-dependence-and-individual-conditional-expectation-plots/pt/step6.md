# Calcular valores de dependência parcial para um recurso específico

```python
x_index = 0
pdp, axes = partial_dependence(model, X, features=[x_index], grid_resolution=20)

# Plotar os valores de dependência parcial
plt.plot(axes[x_index], pdp[0])
plt.xlabel(feature_names[x_index])
plt.ylabel("Dependência Parcial")
plt.title("Gráfico de Dependência Parcial")

plt.show()
```

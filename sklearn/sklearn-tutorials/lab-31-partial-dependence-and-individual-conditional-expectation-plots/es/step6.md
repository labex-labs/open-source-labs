# Calcular los valores de dependencia parcial para una característica específica

```python
x_index = 0
pdp, axes = partial_dependence(model, X, features=[x_index], grid_resolution=20)

# Graficar los valores de dependencia parcial
plt.plot(axes[x_index], pdp[0])
plt.xlabel(feature_names[x_index])
plt.ylabel("Dependencia Parcial")
plt.title("Gráfica de Dependencia Parcial")

plt.show()
```

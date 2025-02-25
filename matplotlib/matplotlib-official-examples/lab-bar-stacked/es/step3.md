# Crear un gráfico de barras apiladas

Crearemos un gráfico de barras apiladas utilizando `matplotlib.pyplot.bar` y recorreremos cada categoría de peso para apilar las barras.

```python
fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Number of penguins with above average body mass")
ax.legend(loc="upper right")
```

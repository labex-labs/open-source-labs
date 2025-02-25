# Crear un gráfico de barras polares

Crearemos un gráfico de barras polares utilizando el parámetro `proyección='polar'`.

```python
ax = plt.subplot(projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)
```

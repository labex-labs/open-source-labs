# Agregar una línea de mejor ajuste

En este paso, agregaremos una línea de mejor ajuste al histograma. Calcularemos los valores de y para la línea y la graficaremos encima del histograma.

```python
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
```

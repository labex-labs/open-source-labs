# Crear un histograma con anchos de contenedor (bins) personalizados

Podemos crear un histograma con anchos de contenedor (bins) personalizados y desiguales proporcionando una lista de bordes de contenedor (bins). En este ejemplo, crearemos un histograma con contenedores (bins) espaciados de manera irregular.

```python
bins = [100, 150, 180, 195, 205, 220, 250, 300]
plt.hist(x, bins=bins, density=True, histtype='bar', rwidth=0.8)
plt.show()
```

# Crear un histograma

En este paso, crearemos un histograma utilizando matplotlib. Estableceremos el número de intervalos en 50 y habilitaremos el parámetro de densidad para normalizar las alturas de los intervalos de modo que la integral del histograma sea 1.

```python
num_bins = 50
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)
```

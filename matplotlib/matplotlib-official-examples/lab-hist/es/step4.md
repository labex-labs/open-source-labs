# Personalizar su histograma

Personalizar un histograma bidimensional es similar al caso unidimensional, puedes controlar componentes visuales como el tamaño del intervalo o la normalización de colores.

```python
fig, axs = plt.subplots(3, 1, figsize=(5, 15), sharex=True, sharey=True,
                        tight_layout=True)

# Podemos aumentar el número de intervalos en cada eje
axs[0].hist2d(dist1, dist2, bins=40)

# Así como definir la normalización de los colores
axs[1].hist2d(dist1, dist2, bins=40, norm=colors.LogNorm())

# También podemos definir números personalizados de intervalos para cada eje
axs[2].hist2d(dist1, dist2, bins=(80, 10), norm=colors.LogNorm())

plt.show()
```

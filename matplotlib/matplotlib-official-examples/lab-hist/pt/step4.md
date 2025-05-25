# Personalizando seu Histograma

Personalizar um histograma 2D é semelhante ao caso 1D, você pode controlar componentes visuais como o tamanho do bin (bin size) ou a normalização de cores.

```python
fig, axs = plt.subplots(3, 1, figsize=(5, 15), sharex=True, sharey=True,
                        tight_layout=True)

# We can increase the number of bins on each axis
axs[0].hist2d(dist1, dist2, bins=40)

# As well as define normalization of the colors
axs[1].hist2d(dist1, dist2, bins=40, norm=colors.LogNorm())

# We can also define custom numbers of bins for each axis
axs[2].hist2d(dist1, dist2, bins=(80, 10), norm=colors.LogNorm())

plt.show()
```

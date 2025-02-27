# Visualizar la segmentación

Visualizaremos las regiones resultantes trazando la imagen original y superponiendo los contornos de las regiones segmentadas.

```python
plt.figure(figsize=(5, 5))
plt.imshow(monedas_redimensionadas, cmap=plt.cm.gray)
plt.xticks(())
plt.yticks(())
title = "Agrupamiento espectral: %s, %.2fs" % (assign_labels, (t1 - t0))
print(title)
plt.title(title)
for l in range(n_regiones):
    colors = [plt.cm.nipy_spectral((l + 4) / float(n_regiones + 4))]
    plt.contour(labels == l, colors=colors)
plt.show()
```

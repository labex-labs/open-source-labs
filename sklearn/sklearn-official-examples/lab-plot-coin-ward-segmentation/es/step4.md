# Representar los resultados

Finalmente, podemos representar los resultados en una imagen. Usaremos matplotlib para representar la imagen escalada y los contornos de los clusters. Recorreremos cada cluster y representaremos el contorno de los píxeles en ese cluster.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(5, 5))
plt.imshow(rescaled_coins, cmap=plt.cm.gray)
for l in range(n_clusters):
    plt.contour(
        label == l,
        colors=[
            plt.cm.nipy_spectral(l / float(n_clusters)),
        ],
    )
plt.axis("off")
plt.show()
```

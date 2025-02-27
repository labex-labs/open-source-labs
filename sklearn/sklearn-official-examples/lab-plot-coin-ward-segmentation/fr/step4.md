# Tracer les résultats

Enfin, nous pouvons tracer les résultats sur une image. Nous utiliserons matplotlib pour tracer l'image redimensionnée et les contours des clusters. Nous parcourrons chaque cluster et traçons le contour des pixels de ce cluster.

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

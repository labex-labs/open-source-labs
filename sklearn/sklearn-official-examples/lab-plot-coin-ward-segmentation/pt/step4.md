# Visualizar os Resultados

Finalmente, podemos visualizar os resultados numa imagem. Usaremos o matplotlib para representar a imagem redimensionada e os contornos dos clusters. Irá percorrer cada cluster e representar o contorno dos pixels nesse cluster.

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

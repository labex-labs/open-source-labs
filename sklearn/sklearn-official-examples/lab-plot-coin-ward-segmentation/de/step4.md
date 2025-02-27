# Ergebnisse plotten

Schließlich können wir die Ergebnisse auf einem Bild plotten. Wir werden matplotlib verwenden, um das skalierten Bild und die Konturen der Cluster zu plotten. Wir werden durch jeden Cluster iterieren und die Kontur der Pixel in diesem Cluster plotten.

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

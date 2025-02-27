# Recréer l'image

Nous allons recréer l'image compressée à l'aide du livre de codes et des étiquettes obtenus à partir du modèle K-Means et du livre de codes aléatoire.

```python
def recreate_image(codebook, labels, w, h):
    """Recréer l'image (compressée) à partir du livre de codes & des étiquettes"""
    return codebook[labels].reshape(w, h, -1)

# Afficher l'image d'origine côte à côte avec les images quantisées
plt.figure()
plt.clf()
plt.axis("off")
plt.title("Image d'origine (96 615 couleurs)")
plt.imshow(china)

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"Image quantisée ({n_colors} couleurs, K-Means)")
plt.imshow(recreate_image(kmeans.cluster_centers_, labels, w, h))

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"Image quantisée ({n_colors} couleurs, Aléatoire)")
plt.imshow(recreate_image(codebook_random, labels_random, w, h))

plt.show()
```

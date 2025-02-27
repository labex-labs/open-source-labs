# Recrear la Imagen

Recrearemos la imagen comprimida utilizando el código y las etiquetas obtenidas del modelo K-Means y el código aleatorio.

```python
def recreate_image(codebook, labels, w, h):
    """Recrear la (comprimida) imagen a partir del libro de códigos & etiquetas"""
    return codebook[labels].reshape(w, h, -1)

# Mostrar la imagen original junto con las imágenes cuantizadas
plt.figure()
plt.clf()
plt.axis("off")
plt.title("Imagen original (96,615 colores)")
plt.imshow(china)

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"Imagen cuantizada ({n_colors} colores, K-Means)")
plt.imshow(recreate_image(kmeans.cluster_centers_, labels, w, h))

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"Imagen cuantizada ({n_colors} colores, Aleatoria)")
plt.imshow(recreate_image(codebook_random, labels_random, w, h))

plt.show()
```

# Recriar a Imagem

Recriaremos a imagem comprimida usando o livro de códigos e as etiquetas obtidas do modelo K-Means e do livro de códigos aleatório.

```python
def recreate_image(codebook, labels, w, h):
    """Recriar a imagem (comprimida) a partir do livro de códigos e etiquetas"""
    return codebook[labels].reshape(w, h, -1)

# Exibir a imagem original juntamente com as imagens quantizadas
plt.figure()
plt.clf()
plt.axis("off")
plt.title("Imagem original (96.615 cores)")
plt.imshow(china)

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"Imagem quantizada ({n_colors} cores, K-Means)")
plt.imshow(recreate_image(kmeans.cluster_centers_, labels, w, h))

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"Imagem quantizada ({n_colors} cores, Aleatório)")
plt.imshow(recreate_image(codebook_random, labels_random, w, h))

plt.show()
```

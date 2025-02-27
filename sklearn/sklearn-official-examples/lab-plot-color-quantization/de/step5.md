# Das Bild neu erstellen

Wir werden das komprimierte Bild mithilfe des Codebuchs und der Labels, die aus dem K-Means-Modell und dem zufälligen Codebuch erhalten wurden, neu erstellen.

```python
def recreate_image(codebook, labels, w, h):
    """Neuerstellt das (komprimierte) Bild aus dem Codebuch & den Labels"""
    return codebook[labels].reshape(w, h, -1)

# Zeigt das Originalbild neben den quantisierten Bildern an
plt.figure()
plt.clf()
plt.axis("off")
plt.title("Originalbild (96.615 Farben)")
plt.imshow(china)

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"Quantisiertes Bild ({n_colors} Farben, K-Means)")
plt.imshow(recreate_image(kmeans.cluster_centers_, labels, w, h))

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"Quantisiertes Bild ({n_colors} Farben, Zufällig)")
plt.imshow(recreate_image(codebook_random, labels_random, w, h))

plt.show()
```

# Redimensionnement d'une image par interpolation 'nearest'

Maintenant, nous allons redimensionner l'image de 500 pixels de données à 530 pixels affichés en utilisant l'interpolation 'nearest'. Cela démontrera comment les motifs de Moiré peuvent encore apparaître même lorsque l'image est redimensionnée si le facteur de redimensionnement n'est pas un nombre entier.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='nearest', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='nearest'")
plt.show()
```

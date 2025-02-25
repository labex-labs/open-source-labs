# Afficher l'image IRM

Nous allons utiliser la fonction `imshow` de `matplotlib` pour afficher l'image IRM en niveaux de gris.

```python
fig, ax = plt.subplots(num="MRI_demo")
ax.imshow(im, cmap="gray")
ax.axis('off')
plt.show()
```

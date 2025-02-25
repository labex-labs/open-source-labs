# Afficher l'image

Maintenant, nous pouvons afficher l'image à l'aide de la méthode `imshow` de Matplotlib. Nous allons également désactiver les axes pour ne voir que l'image.

```python
fig, ax = plt.subplots()
im = ax.imshow(image)
ax.axis('off')
```

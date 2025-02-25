# Créer la représentation graphique

Maintenant que vous avez généré les données, vous allez créer la représentation graphique à l'aide de la fonction `imshow()`.

```python
fig, ax = plt.subplots()
im = ax.imshow(data2d)
ax.set_title('Pan on the colorbar to shift the color mapping\n'
             'Zoom on the colorbar to scale the color mapping')
```

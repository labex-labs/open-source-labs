# Contrôler l'origine de l'image

```python
# Spécifier si les images doivent être tracées avec l'origine du tableau x[0, 0] en haut à gauche ou en bas à droite
x = np.arange(120).reshape((10, 12))

interp = 'bilinear'
fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(3, 5))
axs[0].set_title('le bleu devrait être en haut')
axs[0].imshow(x, origin='upper', interpolation=interp)

axs[1].set_title('le bleu devrait être en bas')
axs[1].imshow(x, origin='lower', interpolation=interp)
plt.show()
```

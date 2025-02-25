# Créer une figure et des axes

Nous allons créer une figure et un objet axe à l'aide de `plt.subplots()`. La fonction `imshow()` est utilisée pour afficher les données aléatoires sous forme d'image.

```python
fig, ax = plt.subplots()

image = np.random.uniform(size=(10, 10))
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('dropped spines')
```

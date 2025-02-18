# Titre en haut

Créez un graphique avec le titre en haut en utilisant la fonction `subplots()` et la fonction `set_xlabel()`.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Top Title')
```

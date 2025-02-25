# Créez le tracé et connectez l'événement de défilement

Nous allons créer le tracé en utilisant la fonction `subplots` de Matplotlib et passer l'objet `IndexTracker` créé à celle-ci. Ensuite, nous allons connecter l'événement de défilement au canevas de la figure en utilisant `mpl_connect`.

```python
fig, ax = plt.subplots()
tracker = IndexTracker(ax, X)

fig.canvas.mpl_connect('scroll_event', tracker.on_scroll)
plt.show()
```

# Créer le tracé Matplotlib

Dans cette étape, nous allons créer un tracé Matplotlib qui affichera nos données. Nous commencerons par créer une figure et en ajouter un sous-graphe.

```python
fig = Figure(figsize=(6, 4))
self.canvas = FigureCanvas(fig)
vbox.pack_start(self.canvas, True, True, 0)
ax = fig.add_subplot()
```

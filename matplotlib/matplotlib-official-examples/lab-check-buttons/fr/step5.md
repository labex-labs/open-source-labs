# Définir la fonction de rappel

Nous devons définir une fonction de rappel pour les boutons de contrôle. Cette fonction sera appelée chaque fois qu'un bouton de contrôle est cliqué. Nous utiliserons cette fonction pour basculer la visibilité de la ligne correspondante sur le graphique.

```python
def callback(label):
    ln = lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    ln.figure.canvas.draw_idle()

check.on_clicked(callback)
```

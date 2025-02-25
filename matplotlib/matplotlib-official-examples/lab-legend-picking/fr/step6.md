# Définir la fonction d'événement de sélection

Nous allons définir la fonction d'événement de sélection qui bascule la visibilité de la ligne d'origine correspondant à la ligne de proxy de la légende.

```python
def on_pick(event):
    # Lors de l'événement de sélection, trouver la ligne d'origine correspondant à la
    # ligne de proxy de la légende, et basculer sa visibilité.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # Changer l'opacité de la ligne dans la légende, afin que l'on puisse voir quelles
    # lignes ont été basculées.
    legline.set_alpha(1.0 si visible sinon 0.2)
    fig.canvas.draw()
```

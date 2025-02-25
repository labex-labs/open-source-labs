# Définissez une fonction pour mettre à jour le second axe

Nous allons définir une fonction de fermeture pour nous enregistrer en tant que rappel pour mettre à jour le second axe en fonction du premier axe.

```python
def convert_ax_c_to_celsius(ax_f):
    """
    Met à jour le second axe en fonction du premier axe.
    """
    y1, y2 = ax_f.get_ylim()
    ax_c.set_ylim(fahrenheit2celsius(y1), fahrenheit2celsius(y2))
    ax_c.figure.canvas.draw()
```

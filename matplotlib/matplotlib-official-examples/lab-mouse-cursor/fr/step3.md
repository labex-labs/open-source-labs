# Définissez le curseur au survol

Nous devons définir le curseur sur le curseur alternatif lorsque l'utilisateur survole un sous-graphique. Nous y parvenons en utilisant l'événement `motion_notify_event` et la fonction `set_cursor()`.

```python
def hover(event):
    if fig.canvas.widgetlock.locked():
        # Ne faites rien si les outils de zoom/déplacement ont été activés.
        return

    fig.canvas.set_cursor(
        event.inaxes.cursor_to_use if event.inaxes else Cursors.POINTER)

fig.canvas.mpl_connect('motion_notify_event', hover)
```

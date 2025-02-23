# Connectez l'événement de dessin à la fonction de rappel

Nous devons connecter l'événement `draw_event` à notre fonction `on_draw`.

```python
fig.canvas.mpl_connect('draw_event', on_draw)
```

# Connecter la fonction d'événement de sélection au canevas

Nous allons connecter la fonction d'événement de sélection au canevas.

```python
fig.canvas.mpl_connect('pick_event', on_pick)
```

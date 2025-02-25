# Connecter les gestionnaires d'événements

Nous allons connecter les gestionnaires d'événements au canevas de la figure.

```python
browser = PointBrowser()

fig.canvas.mpl_connect('pick_event', browser.on_pick)
fig.canvas.mpl_connect('key_press_event', browser.on_press)
```

# Verbinden des Zeichenevents mit der Rückruffunktion

Wir müssen das `draw_event` mit unserer `on_draw`-Funktion verbinden.

```python
fig.canvas.mpl_connect('draw_event', on_draw)
```

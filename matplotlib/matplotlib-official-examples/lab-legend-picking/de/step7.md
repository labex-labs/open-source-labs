# Verbinden der Funktion für das Auslöseereignis beim Auswählen mit der Leinwand

Wir werden die Funktion für das Auslöseereignis beim Auswählen mit der Leinwand verbinden.

```python
fig.canvas.mpl_connect('pick_event', on_pick)
```

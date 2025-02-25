# Festlegen der Tick-Farben

Wir legen die Tick-Farben für jede y-Achse fest, um sie der Farbe der Beschriftungen zu entsprechen.

```python
ax.tick_params(axis='y', colors=p1.get_color())
twin1.tick_params(axis='y', colors=p2.get_color())
twin2.tick_params(axis='y', colors=p3.get_color())
```

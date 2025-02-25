# Achsenstil konfigurieren

Wir werden nun den Achsenstil konfigurieren, indem wir Pfeile am Ende jeder Achse hinzufügen und die X- und Y-Achse vom Ursprung aus hinzufügen.

```python
for direction in ["xzero", "yzero"]:
    # fügt Pfeile am Ende jeder Achse hinzu
    ax.axis[direction].set_axisline_style("-|>")
    # fügt die X- und Y-Achse vom Ursprung aus hinzu
    ax.axis[direction].set_visible(True)

# versteckt die Ränder
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)
```

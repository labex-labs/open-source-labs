# Begrenzungskonditionen für die Keile hinzufügen

Wir fügen Begrenzungskonditionen für die Keile hinzu.

```python
patches += [
    Wedge((.3,.7),.1, 0, 360),             # Vollständiger Kreis
    Wedge((.7,.8),.2, 0, 360, width=0.05),  # Vollständiger Ring
    Wedge((.8,.3),.2, 0, 45),              # Vollständiger Sektor
    Wedge((.8,.3),.2, 45, 90, width=0.10),  # Ringsektor
]
```

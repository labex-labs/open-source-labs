# Definieren einer Funktion, um den Punkt einer gedrehten vertikalen Linie zu erhalten

Wir werden eine Funktion definieren, die die Ursprungskoordinaten, die Linienlänge und den Winkel in Grad als Eingaben nimmt und die xy-Koordinaten des Endpunkts der vertikalen Linie zurückgibt, die um den angegebenen Winkel gedreht ist.

```python
def get_point_of_rotated_vertical(origin, line_length, degrees):
    """Return xy coordinates of the vertical line end rotated by degrees."""
    rad = np.deg2rad(-degrees)
    return [origin[0] + line_length * np.sin(rad),
            origin[1] + line_length * np.cos(rad)]
```

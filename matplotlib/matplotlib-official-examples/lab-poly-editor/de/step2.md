# Erstellen einer Funktion zur Berechnung der Entfernung

Wir müssen eine Funktion erstellen, die die Entfernung zwischen einem Punkt und einem Liniensegment berechnet. Diese Funktion wird später verwendet, um zu bestimmen, ob ein neuer Eckpunkt zum Polygon hinzugefügt werden soll.

```python
def dist_point_to_segment(p, s0, s1):
    """
    Berechnet die Entfernung vom Punkt *p* zum Segment (*s0*, *s1*), wobei
    *p*, *s0*, *s1* ``[x, y]``-Arrays sind.
    """
    s01 = s1 - s0
    s0p = p - s0
    if (s01 == 0).all():
        return np.hypot(*s0p)
    # Projektieren auf das Segment, ohne über die Segmentenden hinauszugehen.
    p1 = s0 + np.clip((s0p @ s01) / (s01 @ s01), 0, 1) * s01
    return np.hypot(*(p - p1))
```

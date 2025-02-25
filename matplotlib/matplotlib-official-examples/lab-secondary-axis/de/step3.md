# Erstellen der Sekundärachse

Wir werden jetzt die Sekundärachse erstellen und die x-Achse von Grad in Radiant umwandeln. Wir werden `deg2rad` als die Vorwärtsfunktion und `rad2deg` als die Umkehrfunktion verwenden.

```python
def deg2rad(x):
    return x * np.pi / 180

def rad2deg(x):
    return x * 180 / np.pi

secax = ax.secondary_xaxis('top', functions=(deg2rad, rad2deg))
secax.set_xlabel('angle [rad]')
```

# Plotten der Daten

Wir werden die in Schritt 2 generierten Zufallsdaten mit der Funktion `plot()` zweimal plotten. Der erste Plot wird einen Alpha-Wert von 0,2 haben und der zweite Plot wird einen Alpha-Wert von 1,0 haben und einen Clip-Pfad auf den gelben Kreis-Patch gesetzt haben.

```python
ax.plot(x, y, alpha=0.2)
line, = ax.plot(x, y, alpha=1.0, clip_path=circ)
ax.set_title("Left click and drag to move looking glass")
```

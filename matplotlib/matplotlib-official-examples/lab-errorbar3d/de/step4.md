# Fehlerbalken zum Diagramm hinzufügen

Wir fügen Fehlerbalken zu unserem Diagramm hinzu, indem wir die `errorbar`-Methode des `Axes3D`-Objekts verwenden. Wir legen die `zuplims`- und `zlolims`-Parameter auf Arrays fest, die angeben, welche Datenpunkte obere und untere Grenzen haben. Wir legen den `errorevery`-Parameter fest, um die Häufigkeit der Fehlerbalken zu steuern.

```python
estep = 15
i = np.arange(t.size)
zuplims = (i % estep == 0) & (i // estep % 3 == 0)
zlolims = (i % estep == 0) & (i // estep % 3 == 2)

ax.errorbar(x, y, z, 0.2, zuplims=zuplims, zlolims=zlolims, errorevery=estep)
```

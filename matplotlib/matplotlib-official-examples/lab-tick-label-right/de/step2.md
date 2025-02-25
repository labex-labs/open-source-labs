# Setze die Standard-Tick-Labels der y-Achse auf der rechten Seite

Wir können die Standard-Tick-Labels der y-Achse auf der rechten Seite des Diagramms mit dem folgenden Code setzen:

```python
plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False
```

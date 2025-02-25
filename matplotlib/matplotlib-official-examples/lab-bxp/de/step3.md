# Boxplot-Statistiken anpassen

Wir können jede der im Schritt 2 berechneten Boxplot-Statistiken ändern. In diesem Beispiel setzen wir die Medianwerte jeder Gruppe auf den Median aller Daten und verdoppeln die Mittelwerte.

```python
for n in range(len(stats)):
    stats[n]['med'] = np.median(data)
    stats[n]['mean'] *= 2
```

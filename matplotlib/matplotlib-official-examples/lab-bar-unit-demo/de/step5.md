# Erstelle das Balkendiagramm

Der nächste Schritt besteht darin, das Balkendiagramm zu erstellen. Wir werden die Funktion `bar()` verwenden, um das Diagramm zu erstellen. Wir werden zwei Sets von Balken erstellen, einen für Tee und einen für Kaffee. Wir werden auch Fehlerbalken zum Diagramm hinzufügen.

```python
ax.bar(ind, tea_means, width, bottom=0*cm, yerr=tea_std, label='Tea')
ax.bar(ind + width, coffee_means, width, bottom=0*cm, yerr=coffee_std,
       label='Coffee')
```

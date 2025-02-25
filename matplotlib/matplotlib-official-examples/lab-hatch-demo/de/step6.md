# Füge einen ellipsenförmigen Pfad mit Schraffierung hinzu

Du kannst auch schraffierte Pfade zu deinem Diagramm hinzufügen. In diesem Fall werden wir die `add_patch`-Funktion verwenden, um einen ellipsenförmigen Pfad zu unserem Diagramm hinzuzufügen.

```python
plt.gca().add_patch(Ellipse((4, 50), 10, 10, fill=True, hatch='*', facecolor='y'))
```

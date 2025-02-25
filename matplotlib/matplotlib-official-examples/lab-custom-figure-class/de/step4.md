# Plotte die Daten mit der benutzerdefinierten Figurunterklasse

Verwende die `plt.figure()`-Funktion, um die Daten mit der benutzerdefinierten Figurunterklasse `WatermarkFigure` zu plotten. In diesem Beispiel fügen wir den Wasserzeichentext "Entwurf" zum Graphen hinzu.

```python
plt.figure(FigureClass=WatermarkFigure, watermark='draft')
plt.plot(x, y)
```

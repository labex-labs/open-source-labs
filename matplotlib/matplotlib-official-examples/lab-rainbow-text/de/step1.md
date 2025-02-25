# Erstes Textobjekt erstellen

Der erste Schritt besteht darin, das erste Textobjekt mit `~.Axes.text` zu erstellen. Dieses Textobjekt wird der Ausgangspunkt für den Konkatenationsprozess sein. Der folgende Code erstellt ein rotes Textobjekt mit dem Wort "Matplotlib" an der Position (0,1, 0,5) auf dem Graphen.

```python
text = ax.text(.1,.5, "Matplotlib", color="red")
```

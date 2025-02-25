# PathPatch-Objekt erstellen

In diesem Schritt erstellen wir ein `PathPatch`-Objekt mit dem Pfad-Objekt, das wir im vorherigen Schritt erstellt haben. Dieses Objekt wird verwendet, um die von dem Pfad eingeschlossene Fläche zu füllen. Wir können auch die Farbe und die Transparenz des Patches festlegen.

```python
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
```

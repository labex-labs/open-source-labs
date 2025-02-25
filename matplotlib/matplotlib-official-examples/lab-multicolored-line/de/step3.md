# Liniensegmente erstellen

Wir werden eine Reihe von Liniensegmenten erstellen, damit wir sie individuell färben können. Wir werden die numpy-Funktion `concatenate` verwenden, um zwei Arrays `points[:-1]` und `points[1:]` entlang der zweiten Achse zusammenzufügen. Anschließend werden wir das resultierende Array in ein N x 1 x 2-Array umformen, damit wir die Punkte leicht zusammenlegen können, um die Segmente zu erhalten. Das Segments-Array für die Linienkollektion muss (numlines) x (Punkte pro Linie) x 2 (für x und y) sein.

```python
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
```

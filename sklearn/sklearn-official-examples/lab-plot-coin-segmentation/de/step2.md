# Konvertiere das Bild in einen Graphen mit dem Wert des Gradienten an den Kanten

Wir werden das Bild in einen Graphen mit dem Wert des Gradienten an den Kanten umwandeln. Je kleiner beta ist, desto unabhängiger ist die Segmentierung von dem tatsächlichen Bild. Für beta = 1 ist die Segmentierung nahezu eine Voronoi-Segmentierung.

```python
# Konvertiere das Bild in einen Graphen mit dem Wert des Gradienten an den
# Kanten.
graph = image.img_to_graph(rescaled_coins)

# Nehme eine abnehmende Funktion des Gradienten: eine Exponentialfunktion
beta = 10
eps = 1e-6
graph.data = np.exp(-beta * graph.data / graph.data.std()) + eps
```

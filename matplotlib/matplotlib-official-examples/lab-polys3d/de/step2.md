# Definieren der Funktion für das Polygon unter dem Graphen

Als nächstes definieren wir eine Funktion `polygon_under_graph(x, y)`, die die Vertex-Liste konstruiert, die das Polygon definiert, das den Raum unter dem (x, y)-Liniendiagramm ausfüllt. Diese Funktion nimmt an, dass x in aufsteigender Reihenfolge vorliegt.

```python
def polygon_under_graph(x, y):
    """
    Konstruiere die Vertex-Liste, die das Polygon definiert, das den Raum unter
    dem (x, y)-Liniendiagramm ausfüllt. Dies setzt voraus, dass x in aufsteigender Reihenfolge vorliegt.
    """
    return [(x[0], 0.), *zip(x, y), (x[-1], 0.)]
```

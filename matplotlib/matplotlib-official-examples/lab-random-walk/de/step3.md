# Definieren der Update-Funktion

Wir definieren eine Funktion, die den Graphen für jedes Frame der Animation aktualisiert. Die Funktion nimmt drei Eingaben entgegen: `num` ist die aktuelle Frame-Nummer, `walks` ist eine Liste aller Zufallswalks und `lines` ist eine Liste aller Linien im Graphen. Für jede Linie und jeden Zufallswalk aktualisieren wir die Daten für die x-, y- und z-Koordinaten der Linie bis zur aktuellen Frame-Nummer. Wir verwenden `line.set_data()` und `line.set_3d_properties()`, um die x-y- und z-Koordinaten jeweils zu aktualisieren.

```python
def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        # NOTE: there is no.set_data() for 3 dim data...
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines
```

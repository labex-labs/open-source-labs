# Graph

## Problem

Implementiere einen Graphen, der die folgenden Anforderungen erfüllt:

### Anforderungen

- Der Graph kann gerichtet oder ungerichtet sein.
- Die Kanten können Gewichte haben.
- Der Graph kann Zyklen enthalten.
- Wenn wir versuchen, einen bereits existierenden Knoten hinzuzufügen, machen wir einfach nichts.
- Wenn wir versuchen, einen nicht existierenden Knoten zu löschen, machen wir einfach nichts.
- Wir können annehmen, dass dies ein zusammenhängender Graph ist.
- Wir können annehmen, dass die Eingaben gültig sind.
- Wir können annehmen, dass dies in den Speicher passt.

## Beispielverwendung

Eingabe:

```
graph.add_edge(0, 1, 5)
graph.add_edge(0, 5, 2)
graph.add_edge(1, 2, 3)
graph.add_edge(2, 3, 4)
graph.add_edge(3, 4, 5)
graph.add_edge(3, 5, 6)
graph.add_edge(4, 0, 7)
graph.add_edge(5, 4, 8)
graph.add_edge(5, 2, 9)
```

Ergebnis:

- Die Knoten `0`, `1`, `2`, `3`, `4` und `5` sind mit den angegebenen Gewichten verbunden.

Hinweis:

- Die Graph-Klasse wird als Baustein für komplexere Graphenaufgaben verwendet.

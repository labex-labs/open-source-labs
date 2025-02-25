# Gitterpfad

## Problem

Gegeben ein rechteckiges Gitter mit gültigen und ungültigen Zellen, implementieren Sie eine Funktion, um einen gültigen Pfad für den Roboter zu finden, um sich von der oberen linken Ecke in die untere rechte Ecke zu bewegen. Wenn es keinen gültigen Pfad gibt, geben Sie None zurück. Wenn die Eingabe ungültig ist oder die Matrix leer ist, geben Sie None zurück.

## Anforderungen

Die Anforderungen für diesen Algorithmus lauten wie folgt:

- Der Roboter kann nur nach rechts und nach unten bewegen.
- Einige Zellen können gesperrt sein.
- Das Gitter ist rechteckig und nicht zickzackig.
- Es muss nicht immer einen gültigen Pfad für den Roboter geben, um die untere rechte Ecke zu erreichen.
- Die Eingabe muss nicht immer gültig sein.
- Der Algorithmus sollte innerhalb der Speicherbeschränkungen passen.

## Beispielverwendung

Betrachten Sie das folgende Gitter:

```txt
o = gültige Zelle
x = ungültige Zelle

   0  1  2  3
0  o  o  o  o
1  o  x  o  o
2  o  o  x  o
3  x  o  o  o
4  o  o  x  o
5  o  o  o  x
6  o  x  o  x
7  o  x  o  o
```

- Allgemeiner Fall:

```txt
erwartet = [(0, 0), (1, 0), (2, 0),
            (2, 1), (3, 1), (4, 1),
            (5, 1), (5, 2), (6, 2),
            (7, 2), (7, 3)]
```

- Kein gültiger Pfad: Im obigen Beispiel ist auch die Zelle in Zeile 7, Spalte 2 ungültig -> None
- Keine Eingabe -> None
- Leere Matrix -> None

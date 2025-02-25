# Bst Validieren

## Problem

Das Problem besteht darin, eine Python-Funktion zu schreiben, die die Wurzel eines binären Baums als Eingabe nimmt und bestimmt, ob es ein gültiger binärer Suchbaum ist. Ein binärer Baum ist genau dann ein gültiger binärer Suchbaum, wenn die folgenden Bedingungen erfüllt sind:

1. Der linke Teilbaum eines Knotens enthält nur Knoten mit Werten, die kleiner als der Wert des Knotens sind.
2. Der rechte Teilbaum eines Knotens enthält nur Knoten mit Werten, die größer als der Wert des Knotens sind.
3. Sowohl der linke als auch der rechte Teilbaum sind selbst gültige binäre Suchbäume.

## Anforderungen

Um diese Herausforderung zu lösen, müssen die folgenden Anforderungen erfüllt sein:

- Die Funktion sollte in der Lage sein, binäre Bäume mit Duplikaten zu verarbeiten.
- Wenn die Funktion mit einer None-Eingabe aufgerufen wird, sollte sie eine Ausnahme auslösen.
- Die Node-Klasse sollte bereits definiert sein.
- Der binäre Baum sollte in den Arbeitsspeicher passen.

## Beispielverwendung

```txt
Gültig:
      5
    /   \
   5     8
  /     /
 4     6
        \
         7

Ungültig:
      5
    /   \
   5     8
  / \   /
 4   9 7
```

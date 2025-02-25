# Baumebenenlisten

## Problem

Gegeben einen binären Suchbaum, erstelle eine Liste für jede Ebene des Baums. Jede Liste sollte die Knoten auf dieser Ebene des Baums enthalten. Die Listen sollten in einem Array von Arrays zurückgegeben werden, wobei jedes Unterarray eine Ebene des Baums repräsentiert.

## Anforderungen

Um dieses Problem zu lösen, müssen die folgenden Anforderungen erfüllt werden:

- Der gegebene Baum ist ein binärer Suchbaum.
- Jede Ebene des Baums sollte durch eine Liste von Knoten repräsentiert werden.
- Es ist bereits eine Node-Klasse mit einer insert-Methode vorhanden.
- Die Lösung sollte in den Speicher passen.

## Beispielverwendung

Zum Beispiel, gegeben der binäre Suchbaum mit den folgenden Werten:

```
5, 3, 8, 2, 4, 1, 7, 6, 9, 10, 11
```

Die Funktion sollte das folgende Array von Arrays zurückgeben:

```
[[5], [3, 8], [2, 4, 7, 9], [1, 6, 10], [11]]
```

Beachte, dass jede Zahl im Ergebnis tatsächlich ein Knoten ist, der die Zahl enthält.

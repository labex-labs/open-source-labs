# Bst Nachfolger

## Problem

Gegeben einen binären Suchbaum und einen Knoten darin, finde den in-order Nachfolger dieses Knotens. Der Nachfolger eines Knotens ist der Knoten, der unmittelbar nach dem gegebenen Knoten in einer in-order Traversierung des Baums erscheint. Wenn es keinen Nachfolger gibt, gebe None zurück. Wenn die Eingabe None ist, werfe eine Ausnahme. Wir können annehmen, dass wir bereits eine Node-Klasse haben, die die Eltern verfolgt, und wir können annehmen, dass dies im Speicher passt.

## Anforderungen

- Die Funktion sollte den in-order Nachfolger eines gegebenen Knotens in einem binären Suchbaum zurückgeben.
- Wenn es keinen Nachfolger gibt, sollte die Funktion None zurückgeben.
- Wenn die Eingabe None ist, sollte die Funktion eine Ausnahme werfen.
- Wir können annehmen, dass wir bereits eine Node-Klasse haben, die die Eltern verfolgt.
- Wir können annehmen, dass dies im Speicher passt.

## Beispielverwendung

```txt
          _5_
        /     \
       3       8
      / \    /   \
     2   4  6    12
    /        \   / \
   1          7 10  15
               /
              9

Eingabe: None  Ausgabe: Ausnahme
Eingabe: 4     Ausgabe: 5
Eingabe: 5     Ausgabe: 6
Eingabe: 8     Ausgabe: 9
Eingabe: 15    Ausgabe: None
```

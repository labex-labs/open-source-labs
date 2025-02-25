# Baum-Breitensuche

## Problem

Gegeben ist ein binärer Baum. Implementieren Sie eine Funktion, die eine Breitensuche auf dem Baum ausführt. Die Funktion sollte bei der Verarbeitung jedes Knotens die Eingabemethode `visit_func` aufrufen.

## Anforderungen

Um dieses Problem zu lösen, müssen die folgenden Anforderungen erfüllt werden:

- Es ist bereits eine `Node`-Klasse mit einer `insert`-Methode vorhanden.
- Die Lösung sollte in den Speicher passen.
- Die `visit_func`-Methode sollte bei der Verarbeitung jedes Knotens aufgerufen werden.

## Beispiel

### Breitensuche

Angenommen, wir haben einen binären Baum mit der folgenden Struktur:

```
    5
   / \
  2   8
 / \
1   3
```

Eine Breitensuche auf diesem Baum würde zu der folgenden Sequenz von besuchten Knoten führen: `5, 2, 8, 1, 3`.

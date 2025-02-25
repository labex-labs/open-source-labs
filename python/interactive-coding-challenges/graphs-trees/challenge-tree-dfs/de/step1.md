# Baum Tiefensuche

## Problem

Implementieren Sie die Tiefendurchläufe (in-order, pre-order, post-order) auf einem binären Baum. Beim in-order-Durchlauf besuchen wir zuerst den linken Unterbaum, dann den aktuellen Knoten und schließlich den rechten Unterbaum. Beim pre-order-Durchlauf besuchen wir zuerst den aktuellen Knoten, dann den linken Unterbaum und schließlich den rechten Unterbaum. Beim post-order-Durchlauf besuchen wir zuerst den linken Unterbaum, dann den rechten Unterbaum und schließlich den aktuellen Knoten.

## Anforderungen

Um diese Herausforderung zu meistern, müssen wir die folgenden Anforderungen erfüllen:

- Wir können davon ausgehen, dass wir bereits eine Node-Klasse mit einer insert-Methode haben.
- Wenn wir jeden Knoten verarbeiten, sollten wir auf dem Knoten eine Eingabe-Methode `visit_func` aufrufen.
- Wir können davon ausgehen, dass dies in den Speicher passt.

## Beispielverwendung

Hier sind einige Beispiele, wie die Tiefensuche-Algorithmus verwendet werden kann:

### In-Order-Durchlauf

Für einen binären Baum mit den Werten 5, 2, 8, 1 und 3 wäre der in-order-Durchlauf 1, 2, 3, 5 und 8. Für einen binären Baum mit den Werten 1, 2, 3, 4 und 5 wäre der in-order-Durchlauf 1, 2, 3, 4 und 5.

### Pre-Order-Durchlauf

Für einen binären Baum mit den Werten 5, 2, 8, 1 und 3 wäre der pre-order-Durchlauf 5, 2, 1, 3 und 8. Für einen binären Baum mit den Werten 1, 2, 3, 4 und 5 wäre der pre-order-Durchlauf 1, 2, 3, 4 und 5.

### Post-Order-Durchlauf

Für einen binären Baum mit den Werten 5, 2, 8, 1 und 3 wäre der post-order-Durchlauf 1, 3, 2, 8 und 5. Für einen binären Baum mit den Werten 1, 2, 3, 4 und 5 wäre der post-order-Durchlauf 5, 4, 3, 2 und 1.

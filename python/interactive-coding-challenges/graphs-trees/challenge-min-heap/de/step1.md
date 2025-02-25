# Min-Heap

## Problem

Implementiere einen Min-Heap mit den folgenden Methoden:

- `extract_min()`: Entfernt und gibt den kleinsten Wert im Heap zurück
- `insert(value)`: Fügt einen neuen Wert in den Heap ein, während die Heap-Eigenschaft beibehalten wird

## Anforderungen

Die Implementierung sollte die folgenden Anforderungen erfüllen:

- Die Eingaben sind Ganzzahlen
- Die Implementierung sollte in den Arbeitsspeicher passen

## Beispielverwendung

Betrachte folgenden Min-Heap:

```txt
          _5_
        /     \
       20     15
      / \    /  \
     22  40 25
```

- `extract_min()`: Entfernt und gibt den kleinsten Wert im Heap zurück, welcher 5 ist. Der resultierende Heap ist:

```txt
          _15_
        /      \
       20      25
      / \     /  \
     22  40
```

- `insert(2)`: Fügt den Wert 2 in den Heap ein, während die Heap-Eigenschaft beibehalten wird. Der resultierende Heap ist:

```txt
          _2_
        /     \
       20      5
      / \     / \
     22  40  25  15
```

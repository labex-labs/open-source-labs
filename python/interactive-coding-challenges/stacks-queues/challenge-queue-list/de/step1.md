# Warteschlangenliste

## Problem

Implementieren Sie eine Warteschlange mit Enqueue- und Dequeue-Methoden mithilfe einer verketteten Liste. Die Enqueue-Methode sollte ein Element am Ende der Warteschlange hinzufügen, und die Dequeue-Methode sollte ein Element von der Anfang der Warteschlange entfernen. Wenn die Warteschlange leer ist, sollte Dequeue None zurückgeben.

## Anforderungen

Um die Warteschlange zu implementieren, müssen wir die folgenden Anforderungen beachten:

- Wenn es ein Element in der Liste gibt, sollten sowohl der erste als auch der letzte Zeiger darauf zeigen.
- Wenn es keine Elemente in der Liste gibt, sollten der erste und der letzte Zeiger None sein.
- Wenn Sie auf eine leere Warteschlange dequeue, sollte None zurückgegeben werden.
- Wir können davon ausgehen, dass dies im Speicher passt.

## Beispielverwendung

### Enqueue

- Enqueue in eine leere Warteschlange: Wenn die Warteschlange leer ist, sollte die Enqueue-Methode das Element als erstes und letztes Element der Warteschlange hinzufügen.
- Enqueue in eine nicht-leere Warteschlange: Wenn die Warteschlange nicht leer ist, sollte die Enqueue-Methode das Element am Ende der Warteschlange hinzufügen.

### Dequeue

- Dequeue von einer leeren Warteschlange -> None: Wenn die Warteschlange leer ist, sollte die Dequeue-Methode None zurückgeben.
- Dequeue von einer Warteschlange mit einem Element: Wenn die Warteschlange nur ein Element hat, sollte die Dequeue-Methode das Element entfernen und die ersten und letzten Zeiger auf None setzen.
- Dequeue von einer Warteschlange mit mehr als einem Element: Wenn die Warteschlange mehr als ein Element hat, sollte die Dequeue-Methode das erste Element entfernen und den ersten Zeiger auf das nächste Element setzen.

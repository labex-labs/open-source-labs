# Stapel (Stack)

## Problem

Implementieren Sie einen Stapel in Python mit einer verketteten Liste mit folgenden Methoden:

- push: Fügt ein Element oben auf den Stapel hinzu
- pop: Entfernt und gibt das Element oben auf dem Stapel zurück. Wenn der Stapel leer ist, wird None zurückgegeben.
- peek: Gibt das Element oben auf dem Stapel zurück, ohne es zu entfernen. Wenn der Stapel leer ist, wird None zurückgegeben.
- is_empty: Gibt True zurück, wenn der Stapel leer ist, andernfalls False.

## Anforderungen

Die folgenden Anforderungen sollten erfüllt werden:

- Wenn ein leerer Stapel gepoppt wird, wird None zurückgegeben.
- Die Implementierung sollte eine verkettete Liste verwenden.
- Die Implementierung sollte in Python erfolgen.
- Die Implementierung sollte die vier Methoden push, pop, peek und is_empty umfassen.

## Beispielverwendung

### Push

- Push auf leeren Stapel: stack.push(1)
- Push auf nicht-leeren Stapel: stack.push(2)

### Pop

- Pop auf leeren Stapel: stack.pop() -> None
- Pop auf Stapel mit einem Element: stack.pop() -> 1
- Pop auf Stapel mit mehreren Elementen: stack.pop() -> 2

### Peek

- Peek auf leeren Stapel: stack.peek() -> None
- Peek auf Stapel mit einem oder mehreren Elementen: stack.peek() -> 2

### Ist leer

- Ist leer auf leeren Stapel: stack.is_empty() -> True
- Ist leer auf Stapel mit einem oder mehreren Elementen: stack.is_empty() -> False

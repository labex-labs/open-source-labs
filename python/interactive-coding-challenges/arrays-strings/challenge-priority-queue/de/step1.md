# Prioritätswarteschlange

## Problem

Implementiere eine Prioritätswarteschlange, die von einem Array unterstützt wird. Die Prioritätswarteschlange sollte die folgenden Methoden unterstützen:

- `insert`: Füge ein neues Element in die Prioritätswarteschlange ein.
- `extract_min`: Entferne und gib das kleinste Element aus der Prioritätswarteschlange zurück.
- `decrease_key`: Verringere den Schlüssel eines angegebenen Elements in der Prioritätswarteschlange.

## Anforderungen

Um die Prioritätswarteschlange zu implementieren, müssen wir die folgenden Anforderungen erfüllen:

- Die von der Prioritätswarteschlange unterstützten Methoden sollten `insert`, `extract_min` und `decrease_key` sein.
- Es sollen keine doppelten Schlüssel in der Prioritätswarteschlange geben.
- Wir müssen keine Eingaben validieren.
- Die Prioritätswarteschlange sollte in den Arbeitsspeicher passen.

## Beispielverwendung

Hier sind einige Beispiele, wie die Methoden der Prioritätswarteschlange verwendet werden können:

### insert

- `insert` im Allgemeinen Fall: Füge einen neuen Knoten in die Prioritätswarteschlange ein.

### extract_min

- `extract_min` aus einer leeren Liste: Gib `None` zurück.
- `extract_min` im Allgemeinen Fall: Entferne und gib den kleinsten Knoten aus der Prioritätswarteschlange zurück.

### decrease_key

- `decrease_key` für einen ungültigen Schlüssel: Gib `None` zurück.
- `decrease_key` im Allgemeinen Fall: Verringere den Schlüssel eines angegebenen Knotens in der Prioritätswarteschlange.

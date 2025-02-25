# Ein Wörterbuch umkehren

## Problem

Schreiben Sie eine Python-Funktion namens `invert_dictionary(obj)`, die ein Wörterbuch `obj` als Argument nimmt und ein neues Wörterbuch zurückgibt, bei dem die Schlüssel und Werte vertauscht sind. Das Eingabewörterbuch `obj` wird einzigartige hashbare Werte haben. Das Ausgabewörterbuch sollte die gleichen Schlüssel wie das Eingabewörterbuch haben, aber die Werte sollten die Schlüssel aus dem Eingabewörterbuch sein.

Sie sollten `dictionary.items()` in Kombination mit einer Listenkomprehension verwenden, um das neue Wörterbuch zu erstellen.

## Beispiel

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: 'Peter', 11: 'Isabel', 9: 'Anna' }
```

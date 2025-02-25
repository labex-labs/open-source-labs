# Ein Wörterbuch umkehren

Schreiben Sie eine Python-Funktion namens `invert_dictionary(obj)`, die ein Wörterbuch `obj` als Argument nimmt und ein neues Wörterbuch zurückgibt, bei dem die Schlüssel und Werte vertauscht sind. Das Eingabe-Wörterbuch `obj` wird einzigartige hashbare Werte haben. Das Ausgabewörterbuch sollte die gleichen Schlüssel wie das Eingabe-Wörterbuch haben, aber die Werte sollten die Schlüssel aus dem Eingabe-Wörterbuch sein.

Sie sollten `dictionary.items()` in Kombination mit einer Listenkomprehension verwenden, um das neue Wörterbuch zu erstellen.

```python
def invert_dictionary(obj):
  return { value: key for key, value in obj.items() }
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: 'Peter', 11: 'Isabel', 9: 'Anna' }
```

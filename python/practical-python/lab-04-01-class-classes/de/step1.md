# Objektorientierte Programmierung

Eine Programmiertechnik, bei der der Code als Sammlung von _Objekten_ organisiert ist.

Ein _Objekt_ besteht aus:

- Daten. Attribute
- Verhalten. Methoden, die als Funktionen auf das Objekt angewendet werden.

Sie haben bereits einige objektorientierte Konzepte in diesem Kurs verwendet.

Zum Beispiel beim Umgang mit einer Liste.

```python
>>> nums = [1, 2, 3]
>>> nums.append(4)      # Methode
>>> nums.insert(1,10)   # Methode
>>> nums
[1, 10, 2, 3, 4]        # Daten
>>>
```

`nums` ist eine _Instanz_ einer Liste.

Methoden (`append()` und `insert()`) sind an die Instanz (`nums`) angehängt.

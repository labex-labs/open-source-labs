# Zusammengesetzte Schlüssel

Fast jeder Wertetyp kann in Python als Wörterbuchschlüssel verwendet werden. Ein Wörterbuchschlüssel muss einen unveränderlichen Typ haben. Beispielsweise Tupel:

```python
holidays = {
  (1, 1) : 'Neujahr',
  (3, 14) : 'Pi Tag',
  (9, 13) : "Programmierer-Tag",
}
```

Dann um darauf zuzugreifen:

```python
>>> holidays[3, 14]
'Pi Tag'
>>>
```

_Weder eine Liste, ein Set noch ein weiteres Wörterbuch kann als Wörterbuchschlüssel dienen, da Listen und Wörterbücher veränderlich sind._

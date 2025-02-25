# zip()-Funktion

Die `zip`-Funktion nimmt mehrere Sequenzen entgegen und erstellt einen Iterator, der sie kombiniert.

```python
columns = ['name','shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
# ('name','GOOG'), ('shares',100), ('price',490.1)
```

Um das Ergebnis zu erhalten, müssen Sie iterieren. Sie können wie zuvor mehrere Variablen verwenden, um die Tupel aufzulösen.

```python
for column, value in pairs:
  ...
```

Eine häufige Verwendung von `zip` ist das Erstellen von Schlüssel/Wert-Paaren zum Erstellen von Dictionaries.

```python
d = dict(zip(columns, values))
```

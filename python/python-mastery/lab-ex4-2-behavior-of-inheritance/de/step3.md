# Verwenden Ihrer Validatoren

Ihre Validatoren können verwendet werden, um Wertprüfungen für Funktionen und Klassen hinzuzufügen. Beispielsweise könnten die Validatoren vielleicht in den Eigenschaften von `Stock` verwendet werden:

```python
class Stock:
  ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)
  ...
```

Kopieren Sie die `Stock`-Klasse aus `stock.py` und ändern Sie sie, um die Validatoren im Eigenschaftscode für `shares` und `price` zu verwenden.

# Standardargumente

Manchmal möchten Sie, dass ein Argument optional ist. Wenn so, weisen Sie im Funktionsdefinition einen Standardwert zu.

```python
def read_prices(filename, debug=False):
 ...
```

Wenn ein Standardwert zugewiesen ist, ist das Argument in Funktionsaufrufen optional.

```python
d = read_prices('prices.csv')
e = read_prices('prices.dat', True)
```

_Hinweis: Argumente mit Standardwerten müssen am Ende der Argumentliste stehen (alle nicht-optionalen Argumente kommen zuerst)._

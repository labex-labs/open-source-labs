# Liste sortieren - erneute Betrachtung

Listen können _in-place_ sortiert werden. Mit der `sort`-Methode.

```python
s = [10,1,7,3]
s.sort() # s = [1,3,7,10]
```

Man kann in umgekehrter Reihenfolge sortieren.

```python
s = [10,1,7,3]
s.sort(reverse=True) # s = [10,7,3,1]
```

Das scheint einfach genug zu sein. Wie sortieren wir jedoch eine Liste von Wörterbüchern?

```python
[{'name': 'AA', 'price': 32.2,'shares': 100},
{'name': 'IBM', 'price': 91.1,'shares': 50},
{'name': 'CAT', 'price': 83.44,'shares': 150},
{'name': 'MSFT', 'price': 51.23,'shares': 200},
{'name': 'GE', 'price': 40.37,'shares': 95},
{'name': 'MSFT', 'price': 65.1,'shares': 50},
{'name': 'IBM', 'price': 70.44,'shares': 100}]
```

Nach welchen Kriterien?

Man kann die Sortierung durch Verwendung einer _Schlüsselfunktion_ steuern. Die _Schlüsselfunktion_ ist eine Funktion, die das Wörterbuch erhält und den für die Sortierung interessanten Wert zurückgibt.

```python
portfolio = [
    {'name': 'AA', 'price': 32.2,'shares': 100},
    {'name': 'IBM', 'price': 91.1,'shares': 50},
    {'name': 'CAT', 'price': 83.44,'shares': 150},
    {'name': 'MSFT', 'price': 51.23,'shares': 200},
    {'name': 'GE', 'price': 40.37,'shares': 95},
    {'name': 'MSFT', 'price': 65.1,'shares': 50},
    {'name': 'IBM', 'price': 70.44,'shares': 100}
]

def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)
```

Hier ist das Ergebnis.

```python
# Überprüfen, wie die Wörterbücher nach dem `name`-Schlüssel sortiert werden
[
  {'name': 'AA', 'price': 32.2,'shares': 100},
  {'name': 'CAT', 'price': 83.44,'shares': 150},
  {'name': 'GE', 'price': 40.37,'shares': 95},
  {'name': 'IBM', 'price': 91.1,'shares': 50},
  {'name': 'IBM', 'price': 70.44,'shares': 100},
  {'name': 'MSFT', 'price': 51.23,'shares': 200},
  {'name': 'MSFT', 'price': 65.1,'shares': 50}
]
```

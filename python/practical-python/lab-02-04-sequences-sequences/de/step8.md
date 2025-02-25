# Schleifen über ganze Zahlen

Wenn Sie zählen müssen, verwenden Sie `range()`.

```python
for i in range(100):
    # i = 0,1,...,99
```

Die Syntax lautet `range([start,] end [,step])`

```python
for i in range(100):
    # i = 0,1,...,99
for j in range(10,20):
    # j = 10,11,..., 19
for k in range(10,50,2):
    # k = 10,12,...,48
    # Beachten Sie, wie es in Schritten von 2 zählt, nicht 1.
```

- Der Endwert wird niemals eingeschlossen. Es spiegelt das Verhalten von Slices wider.
- `start` ist optional. Standardwert `0`.
- `step` ist optional. Standardwert `1`.
- `range()` berechnet Werte nach Bedarf. Es speichert tatsächlich keine großen Zahlenbereiche.

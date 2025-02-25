# Schleifen

Die `while`-Anweisung führt eine Schleife aus.

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Anzahl der Tage', day)
```

Die eingerückten Anweisungen unterhalb der `while` werden solange ausgeführt, wie der Ausdruck nach der `while` `true` ist.

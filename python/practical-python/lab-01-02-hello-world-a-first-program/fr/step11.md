# Boucles

L'instruction `while` exécute une boucle.

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

Les instructions indentées sous le `while` seront exécutées tant que l'expression après le `while` est `vraie`.

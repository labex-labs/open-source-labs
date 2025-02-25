# Bucle

La instrucción `while` ejecuta un bucle.

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

Las instrucciones indentadas debajo de `while` se ejecutarán siempre que la expresión después de `while` sea `true`.

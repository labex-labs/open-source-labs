# Mejores prácticas de sangría

- Utilice espacios en lugar de tabulaciones.
- Utilice 4 espacios por nivel.
- Utilice un editor compatible con Python.

La única exigencia de Python es que la sangría dentro del mismo bloque sea consistente. Por ejemplo, esto es un error:

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
        day = day + 1 # ERROR
    num_bills = num_bills * 2
```

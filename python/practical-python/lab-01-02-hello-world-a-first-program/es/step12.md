# Sangría

La sangría se utiliza para denotar grupos de instrucciones que van juntas. Considere el ejemplo anterior:

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

La sangría agrupa las siguientes instrucciones juntas como las operaciones que se repiten:

```python
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2
```

Debido a que la instrucción `print()` al final no está sangrada, no pertenece al bucle. La línea en blanco es solo para la legibilidad. No afecta la ejecución.

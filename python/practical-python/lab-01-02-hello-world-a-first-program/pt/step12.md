# Indentação (Indentation)

A indentação é usada para denotar grupos de instruções que pertencem juntas. Considere o exemplo anterior:

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

A indentação agrupa as seguintes instruções como as operações que se repetem:

```python
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2
```

Como a instrução `print()` no final não está indentada, ela não pertence ao laço (loop). A linha em branco é apenas para legibilidade. Ela não afeta a execução.

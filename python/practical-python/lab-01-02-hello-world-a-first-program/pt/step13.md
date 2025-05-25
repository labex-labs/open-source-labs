# Melhores práticas de indentação (Indentation best practices)

- Use espaços em vez de tabs.
- Use 4 espaços por nível.
- Use um editor que reconheça Python.

O único requisito do Python é que a indentação dentro do mesmo bloco seja consistente. Por exemplo, isto é um erro:

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
        day = day + 1 # ERROR
    num_bills = num_bills * 2
```

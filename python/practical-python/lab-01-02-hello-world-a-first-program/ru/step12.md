# Отступы

Отступы используются для обозначения групп инструкций, которые относятся к одному блоку. Рассмотрим предыдущий пример:

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

Отступы объединяют следующие инструкции в группы операций, которые повторяются:

```python
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2
```

Поскольку инструкция `print()` в конце не имеет отступа, она не относится к циклу. Пустая строка нужна только для улучшения читаемости. Она не влияет на выполнение программы.

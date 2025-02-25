# Циклы

Инструкция `while` выполняет цикл.

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

Инструкции, отступившиеся ниже `while`, будут выполняться, пока выражение после `while` истинно.

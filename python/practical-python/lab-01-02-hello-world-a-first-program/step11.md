# Looping

The `while` statement executes a loop.

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

The statements indented below the `while` will execute as long as the expression after the `while` is `true`.

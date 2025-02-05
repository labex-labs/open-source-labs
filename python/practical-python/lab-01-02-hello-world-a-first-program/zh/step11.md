# 循环

`while` 语句用于执行循环。

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

只要 `while` 后面的表达式为 `真`，缩进在 `while` 下面的语句就会执行。

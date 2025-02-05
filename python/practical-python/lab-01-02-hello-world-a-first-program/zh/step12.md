# 缩进

缩进用于表示属于同一组的语句。看前面的例子：

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

缩进将以下语句组合在一起，作为重复执行的操作：

```python
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2
```

因为末尾的 `print()` 语句没有缩进，所以它不属于循环。空行只是为了提高可读性，不影响执行。

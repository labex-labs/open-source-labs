# ループ

`while` 文はループを実行します。

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

`while` の下にインデントされた文は、`while` の後の式が `true` の間実行されます。

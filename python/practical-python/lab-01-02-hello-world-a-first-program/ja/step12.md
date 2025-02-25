# インデント

インデントは、一緒になる文のグループを表すために使用されます。前の例を見てみましょう。

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

インデントにより、次の文が反復する操作としてグループ化されます。

```python
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2
```

最後の `print()` 文はインデントされていないため、ループに属しません。空行は読みやすさのためだけのもので、実行には影響しません。

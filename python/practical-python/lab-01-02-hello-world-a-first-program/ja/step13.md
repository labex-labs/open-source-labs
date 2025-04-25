# インデントのベストプラクティス

- タブではなく半角スペースを使用します。
- 1 段階あたり 4 つの半角スペースを使用します。
- Python に対応したエディタを使用します。

Python の唯一の要件は、同じブロック内のインデントが一貫していることです。たとえば、これはエラーです。

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
        day = day + 1 # エラー
    num_bills = num_bills * 2
```

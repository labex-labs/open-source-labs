# インデントのベストプラクティス

- タブではなく半角スペースを使用します。
- 1段階あたり4つの半角スペースを使用します。
- Pythonに対応したエディタを使用します。

Pythonの唯一の要件は、同じブロック内のインデントが一貫していることです。たとえば、これはエラーです。

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
        day = day + 1 # エラー
    num_bills = num_bills * 2
```

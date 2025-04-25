# レコード配列を構造化配列に変換する

レコード配列を構造化配列に戻すには、`view` メソッドを使って構造化配列の元の dtype を指定することができます。

```python
# Convert a record array to a structured array
x = recordarr.view(dtype=[('name', 'U10'), ('age', int)])
```

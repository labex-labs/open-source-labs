# 構造化配列をレコード配列に変換する

`view` メソッドを使って、構造化配列を `np.recarray` 型を指定してレコード配列に変換することができます。

```python
# Convert a structured array to a record array
recordarr = x.view(np.recarray)
```

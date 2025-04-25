# レコード配列の作成

レコード配列は、ndarray のサブクラスであり、インデックスではなく属性を使ってフィールドにアクセスできるようにします。`np.rec.array`関数を使ってレコード配列を作成することができます。

```python
# Create a record array
recordarr = np.rec.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```

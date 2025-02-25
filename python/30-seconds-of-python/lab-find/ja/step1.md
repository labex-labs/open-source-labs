# 一致する値を見つける

`find(lst, fn)` という名前の関数を書きます。この関数は、リスト `lst` とテスト関数 `fn` を引数として受け取ります。この関数は、`fn` が `True` を返す `lst` の最初の要素の値を返す必要があります。もし要素がテスト関数を満たさなければ、関数は `None` を返す必要があります。

```python
def find(lst, fn):
  return next(x for x in lst if fn(x))
```

```python
find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
```

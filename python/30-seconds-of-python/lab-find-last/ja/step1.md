# 最後の一致する値を見つける

引数としてリスト `lst` とテスト関数 `fn` を受け取る関数 `find_last(lst, fn)` を書きます。この関数は、`fn` が `True` を返す `lst` の最後の要素の値を返す必要があります。どの要素もテスト関数を満たさない場合、関数は `None` を返す必要があります。

この問題を解くには、リスト内包表記と `next()` を使って、リストを逆順に反復処理し、テスト関数を満たす最後の要素を返します。

```python
def find_last(lst, fn):
  return next(x for x in lst[::-1] if fn(x))
```

```python
find_last([1, 2, 3, 4], lambda n: n % 2 == 1) # 3
```

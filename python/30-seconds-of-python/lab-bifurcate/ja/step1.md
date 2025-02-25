# リストを二つに分ける

`bifurcate(lst, filter)` という関数を書きましょう。この関数は、リスト `lst` とフィルター `filter` を入力として受け取り、二つのリストからなるリストを返します。最初のリストはフィルターを通過する `lst` の要素を含み、二番目のリストは通過しない要素を含む必要があります。

この関数を実装するには、リスト内包表記と `zip()` 関数を使うことができます。`zip()` 関数は二つ以上のリストを入力として受け取り、各リストからの対応する要素を含むタプルのリストを返します。たとえば、`zip([1, 2, 3], [4, 5, 6])` は `[(1, 4), (2, 5), (3, 6)]` を返します。

この関数を使って、`lst` と `filter` の両方を同時に反復処理し、フィルターを通過するかどうかに基づいて要素を適切なリストに追加することができます。

```python
def bifurcate(lst, filter):
  return [
    [x for x, flag in zip(lst, filter) if flag],
    [x for x, flag in zip(lst, filter) if not flag]
  ]
```

```python
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```

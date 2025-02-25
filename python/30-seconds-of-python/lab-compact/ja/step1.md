# コンパクトなリスト

引数としてリストを受け取り、すべての偽の値が削除された新しいリストを返す関数`compact(lst)`を書きます。偽の値には`False`、`None`、`0`、および`""`が含まれます。

この問題を解決するには、`filter()`関数を使用してリストから偽の値をフィルタリングできます。

```python
def compact(lst):
  return list(filter(None, lst))
```

```python
compact([0, 1, False, 2, '', 3, 'a','s', 34]) # [ 1, 2, 3, 'a','s', 34 ]
```

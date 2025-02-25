# 辞書のリストから値を抜き出す

`pluck(lst, key)` という関数を書きます。この関数は、辞書のリスト `lst` とキー `key` を引数として受け取り、指定された `key` に対応する値のリストを返します。

以下のことが必要です。

- リスト内包表記と `dict.get()` を使って、`lst` 内の各辞書の `key` の値を取得します。
- 入力リストが空の場合、または指定されたキーがどの辞書にも存在しない場合、関数は空のリストを返す必要があります。

```python
def pluck(lst, key):
  return [x.get(key) for x in lst]
```

```python
simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name':'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]
pluck(simpsons, 'age') # [8, 36, 34, 10]
```

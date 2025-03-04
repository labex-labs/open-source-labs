# 辞書のリストから値を抜き出す

## 問題

`pluck(lst, key)` という関数を書きましょう。この関数は、辞書のリスト `lst` とキー `key` を引数として受け取り、指定された `key` に対応する値のリストを返します。

次のことが必要です。

- リスト内包表記と `dict.get()` を使って、`lst` 内の各辞書に対する `key` の値を取得する。
- 入力リストが空の場合、または指定されたキーがどの辞書にも存在しない場合、関数は空のリストを返す。

## 例

```python
simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name':'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]
print(pluck(simpsons, 'age')) # [8, 36, 34, 10]
```

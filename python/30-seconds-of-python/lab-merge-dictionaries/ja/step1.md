# 辞書のマージ

2つ以上の辞書を引数として受け取り、入力辞書のすべてのキーと値のペアを含む新しい辞書を返す関数 `merge_dictionaries(*dicts)` を作成してください。

あなたの関数は新しい辞書を作成し、入力辞書をループして、各辞書のキーと値のペアを `dictionary.update()` を使って結果に追加する必要があります。

```python
def merge_dictionaries(*dicts):
  res = dict()
  for d in dicts:
    res.update(d)
  return res
```

```python
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
```

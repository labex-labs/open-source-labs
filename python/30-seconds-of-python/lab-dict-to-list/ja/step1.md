# 辞書からリストへ

辞書 `d` を引数として受け取り、タプルのリストを返す関数 `dict_to_list(d)` を書きます。各タプルは、辞書のキーと値のペアを含む必要があります。リスト内のタプルの順序は、辞書内のキーと値のペアの順序と同じでなければなりません。

```python
def dict_to_list(d):
  return list(d.items())
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
dict_to_list(d)
# [('one', 1), ('three', 3), ('five', 5), ('two', 2), ('four', 4)]
```

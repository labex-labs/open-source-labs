# 辞書の値をマッピングする

`map_values(obj, fn)` という関数を書きなさい。この関数は、辞書 `obj` と関数 `fn` を引数として取り、元の辞書と同じキーを持ち、各値に対して提供された関数を実行することで生成された値を持つ新しい辞書を返します。

```python
def map_values(obj, fn):
  return dict((k, fn(v)) for k, v in obj.items())
```

```python
users = {
  'fred': { 'user': 'fred', 'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
}
map_values(users, lambda u : u['age']) # {'fred': 40, 'pebbles': 1}
```

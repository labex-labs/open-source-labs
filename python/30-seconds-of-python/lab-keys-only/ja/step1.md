# 辞書のキー

入力としてフラットな辞書を受け取り、そのすべてのキーのリストを返す関数 `keys_only(flat_dict)` を作成します。

この問題を解決するには、次の手順に従うことができます。

1. `dict.keys()` を使用して、与えられた辞書のキーを返します。
2. 前の結果の `list()` を返します。

```python
def keys_only(flat_dict):
  return list(flat_dict.keys())
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```

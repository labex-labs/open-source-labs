# 辞書のキー

## 問題

`keys_only(flat_dict)` という関数を書きなさい。この関数は、フラットな辞書を入力として受け取り、そのすべてのキーのリストを返します。

この問題を解くには、次の手順に従うことができます。

1. `dict.keys()` を使用して、与えられた辞書のキーを返します。
2. 前の結果の `list()` を返します。

## 例

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```

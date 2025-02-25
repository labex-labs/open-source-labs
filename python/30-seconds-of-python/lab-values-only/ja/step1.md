# 辞書の値

フラットな辞書が与えられ、辞書内のすべての値のフラットなリストを返す関数を作成する必要があります。あなたのタスクは、`values_only(flat_dict)`関数を実装することです。この関数は、フラットな辞書を引数として受け取り、辞書内のすべての値のリストを返します。

この問題を解決するには、与えられた辞書の値を返すために`dict.values()`メソッドを使用できます。その後、`list()`関数を使用して結果をリストに変換できます。

```python
def values_only(flat_dict):
  return list(flat_dict.values())
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
values_only(ages) # [10, 11, 9]
```

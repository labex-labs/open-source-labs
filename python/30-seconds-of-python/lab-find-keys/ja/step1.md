# 値を持つキーを見つける

`find_keys(dictionary, value)` というPython関数を書きます。この関数は辞書と値を引数として受け取り、与えられた値を持つ辞書内のすべてのキーのリストを返します。与えられた値を持つキーがない場合、関数は空のリストを返す必要があります。

この問題を解くには、辞書のキー-値ペアを生成するジェネレータを返す `dictionary.items()` メソッドを使用できます。その後、与えられた値を持つキーをフィルタリングするためにリスト内包表記を使用できます。

```python
def find_keys(dict, val):
  return list(key for key, value in dict.items() if value == val)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
find_keys(ages, 10) # [ 'Peter', 'Anna' ]
```

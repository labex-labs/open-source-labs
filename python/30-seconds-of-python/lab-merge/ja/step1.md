# リストをマージする

`merge(*args, fill_value=None)` という名前の関数を書きます。この関数は 2 つ以上のリストを引数として受け取り、リストのリストを返します。関数は、入力リストそれぞれの要素を位置に基づいて結合する必要があります。もしあるリストが最長のリストより短い場合、関数は残りの要素に対して `fill_value` を使う必要があります。`fill_value` が提供されない場合、デフォルト値は `None` になります。

あなたのタスクは `merge()` 関数を実装することです。

```python
def merge(*args, fill_value = None):
  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    ])
  return result
```

```python
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```

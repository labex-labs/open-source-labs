# 値でリストを初期化する

`initialize_list_with_values(n, val=0)` という関数を書きます。この関数には 2 つのパラメータが渡されます。

- `n`（整数）は作成するリストの長さを表します。
- `val`（整数）はリストを埋めるために使用する値を表します。`val` が指定されない場合、デフォルト値の `0` が使用されます。

この関数は、指定された値で埋められた長さ `n` のリストを返す必要があります。

```python
def initialize_list_with_values(n, val = 0):
  return [val for x in range(n)]
```

```python
initialize_list_with_values(5, 2) # [2, 2, 2, 2, 2]
```

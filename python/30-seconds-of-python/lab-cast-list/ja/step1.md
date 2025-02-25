# リストにキャスト

引数として値を受け取り、それをリストとして返す関数 `cast_list(val)` を作成します。値が既にリストである場合は、そのまま返します。値がリストではないがイテラブルな場合は、リストとして返します。値がイテラブルでない場合は、単一要素のリストとして返します。

```python
def cast_list(val):
  return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]
```

```python
cast_list('foo') # ['foo']
cast_list([1]) # [1]
cast_list(('foo', 'bar')) # ['foo', 'bar']
```

# 最長の要素

任意の数の反復可能なオブジェクトまたは長さプロパティを持つオブジェクトを引数として受け取り、最長のものを返す関数`longest_item(*args)`を書きなさい。この関数は以下のことを行う必要があります。

- `max()`を`len()`とともに`key`として使用して、最長の要素を返す。
- 複数の要素が同じ長さの場合、最初の要素を返す。

```python
def longest_item(*args):
  return max(args, key = len)
```

```python
longest_item('this', 'is', 'a', 'testcase') # 'testcase'
longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
longest_item([1, 2, 3], 'foobar') # 'foobar'
```

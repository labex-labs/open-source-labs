# 反復処理: プロトコル

`for` 文を考えてみましょう。

```python
for x in obj:
    # 文
```

内部で何が起こるのでしょうか。

```python
_iter = obj.__iter__()        # イテレータオブジェクトを取得する
while True:
    try:
        x = _iter.__next__()  # 次の要素を取得する
        # 文...
    except StopIteration:     # 要素がもうない
        break
```

`for` ループで動作するすべてのオブジェクトは、この低レベルの反復処理プロトコルを実装しています。

例: リストの手動反復処理。

```python
>>> x = [1,2,3]
>>> it = x.__iter__()
>>> it
<listiterator object at 0x590b0>
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in? StopIteration
>>>
```

# リスト内の n 番目の要素

`every_nth(lst, nth)` という関数を書きましょう。この関数は、リスト `lst` と整数 `nth` を引数として受け取り、元のリストの「n 番目」の要素をすべて含む新しいリストを返します。

```python
def every_nth(lst, nth):
  return lst[nth - 1::nth]
```

```python
every_nth([1, 2, 3, 4, 5, 6], 2) # [ 2, 4, 6 ]
```

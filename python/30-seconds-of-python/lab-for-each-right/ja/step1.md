# 逆順で各リスト要素に対して関数を実行する

`for_each_right(itr, fn)` という関数を書きます。この関数は、リスト `itr` と関数 `fn` を引数とします。この関数は、`itr` の各要素に対して `fn` を最後の要素から始めて 1 回ずつ実行する必要があります。

```python
def for_each_right(itr, fn):
  for el in itr[::-1]:
    fn(el)
```

```python
for_each_right([1, 2, 3], print) # 3 2 1
```

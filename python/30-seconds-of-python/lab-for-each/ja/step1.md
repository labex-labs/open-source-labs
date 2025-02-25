# 各リスト要素に対して関数を実行する

引数としてリスト `itr` と関数 `fn` を受け取る関数 `for_each(itr, fn)` を書きます。この関数は、`itr` の各要素に対して `fn` を1回実行する必要があります。

```python
def for_each(itr, fn):
  for el in itr:
    fn(el)
```

```python
for_each([1, 2, 3], print) # 1 2 3
```

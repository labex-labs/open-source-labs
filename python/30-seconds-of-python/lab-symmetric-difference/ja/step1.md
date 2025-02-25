# 対称差

2 つのリストを引数として受け取り、それらの対称差をリストとして返す関数 `symmetric_difference(a, b)` を書きます。この関数は重複する値をフィルタリングしないものとします。

この問題を解くには、次の手順をたどることができます。

1. それぞれのリストからセットを作成します。
2. それぞれのセットに対して、他方のセットに含まれていない値のみを残すためのリスト内包表記を使用します。
3. 手順 2 で得られた 2 つのリストを連結します。

```python
def symmetric_difference(a, b):
  (_a, _b) = (set(a), set(b))
  return [item for item in a if item not in _b] + [item for item in b
          if item not in _a]
```

```python
symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]
```

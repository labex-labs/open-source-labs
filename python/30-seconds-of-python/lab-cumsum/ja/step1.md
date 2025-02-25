# 部分和のリスト

`partial_sum(lst)` という関数を書きましょう。この関数は、数値のリストを引数として受け取り、部分和のリストを返します。あなたの関数は以下の手順を実行する必要があります。

1. `itertools.accumulate()` を使って、リストの各要素に対する累積和を作成します。
2. `list()` を使って、結果をリストに変換します。
3. 部分和のリストを返します。

```python
from itertools import accumulate

def cumsum(lst):
  return list(accumulate(lst))
```

```python
cumsum(range(0, 15, 3)) # [0, 3, 9, 18, 30]
```

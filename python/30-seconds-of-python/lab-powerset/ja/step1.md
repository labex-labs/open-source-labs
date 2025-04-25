# 冪集合

`powerset(iterable)` という名前の Python 関数を書きます。この関数は、反復可能オブジェクトを引数として受け取り、その反復可能オブジェクトの冪集合を返します。この関数は以下の手順に従う必要があります。

1. 与えられた値をリストに変換します。
2. `range()` と `itertools.combinations()` を使用して、すべての部分集合を返すジェネレータを作成します。
3. `itertools.chain.from_iterable()` と `list()` を使用して、ジェネレータを消費してリストを返します。

```python
from itertools import chain, combinations

def powerset(iterable):
  s = list(iterable)
  return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
```

```python
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]
```

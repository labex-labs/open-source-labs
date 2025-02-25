# 深くフラット化されたリスト

引数としてリスト `lst` を受け取り、`lst` の深くフラット化されたバージョンである新しいリストを返す関数 `deep_flatten(lst)` を書きます。この関数は再帰を使用し、要素が反復可能かどうかを確認するために `collections.abc.Iterable` を使った `isinstance()` 関数を使用する必要があります。要素が反復可能な場合、関数は再帰的に `deep_flatten()` をその要素に適用する必要があります。それ以外の場合、関数はその要素のみを含むリストを返す必要があります。

```python
from collections.abc import Iterable

def deep_flatten(lst):
  return ([a for i in lst for a in
          deep_flatten(i)] if isinstance(lst, Iterable) else [lst])
```

```python
deep_flatten([1, [2], [[3], 4], 5]) # [1, 2, 3, 4, 5]
```

# 重複しないリスト値をフィルタリングする

`filter_non_unique(lst)` という名前の Python 関数を書きます。この関数は引数としてリストを受け取り、重複しない値のみを含む新しいリストを返します。この問題を解くには、次の手順に従うことができます。

1. `collections.Counter` メソッドを使用して、リスト内の各値の出現回数を取得します。
2. 重複しない値のみを含むリストを作成するために、リスト内包表記を使用します。

```python
from collections import Counter

def filter_non_unique(lst):
  return [item for item, count in Counter(lst).items() if count == 1]
```

```python
filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]
```

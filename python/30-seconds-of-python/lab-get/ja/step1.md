# ネストされた値を取得する

辞書またはリスト `d` とセレクターのリスト `selectors` を引数として受け取り、与えられたセレクターのリストによって示されるネストされたキーの値を返す関数 `get(d, selectors)` を書きます。キーが存在しない場合は `None` を返します。

この関数を実装するには、`functools.reduce()` を使って `selectors` リストを反復処理します。`selectors` の各キーに対して `operator.getitem()` を適用し、次の反復処理のイテレータとして使用する値を取得します。

```python
from functools import reduce
from operator import getitem

def get(d, selectors):
  return reduce(getitem, selectors, d)
```

```python
users = {
  'freddy': {
    'name': {
      'first': 'fred',
      'last':'smith'
    },
    'postIds': [1, 2, 3]
  }
}
get(users, ['freddy', 'name', 'last']) #'smith'
get(users, ['freddy', 'postIds', 1]) # 2
```

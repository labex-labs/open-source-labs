# ネストされた値を取得する

## 問題

辞書またはリスト `d` とセレクターのリスト `selectors` を引数として受け取り、与えられたセレクター リストによって示されるネストされたキーの値を返す関数 `get(d, selectors)` を作成します。キーが存在しない場合は `None` を返します。

この関数を実装するには、`functools.reduce()` を使用して `selectors` リストを反復処理します。`selectors` の各キーに対して `operator.getitem()` を適用し、次の反復処理のイテレータとして使用する値を取得します。

## 例

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
get(users, ['freddy', 'age']) # None
```

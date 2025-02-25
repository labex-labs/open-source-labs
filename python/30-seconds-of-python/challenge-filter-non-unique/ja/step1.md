# 重複しないリスト値のフィルタリング

## 問題

引数としてリストを受け取り、重複しない値のみを含む新しいリストを返す、`filter_non_unique(lst)` という Python 関数を作成してください。この問題を解くには、次の手順に従うことができます。

1. `collections.Counter` メソッドを使用して、リスト内の各値のカウントを取得します。
2. 重複しない値のみを含むリストを作成するために、リスト内包表記を使用します。

## 例

```python
filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]
filter_non_unique(['apple', 'banana', 'apple', 'orange', 'pear', 'banana']) # ['orange', 'pear']
```

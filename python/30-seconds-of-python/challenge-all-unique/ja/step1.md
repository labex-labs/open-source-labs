# リスト関数の重複チェック

## 問題

引数としてリストを受け取り、リストに重複する要素があれば `True` を返し、そうでなければ `False` を返す、`has_duplicates(lst)` という Python 関数を書きなさい。

この問題を解くには、次の手順に従うことができます。

1. 重複を削除するためにリストをセットに変換します。
2. セットの長さと元のリストの長さを比較します。
3. 長さが等しい場合、リストには重複する要素がなく、そうでなければ重複する要素があります。

## 例

```python
has_duplicates([1, 2, 3, 4, 5]) # False
has_duplicates([1, 2, 3, 4, 5, 5]) # True
has_duplicates(['apple', 'banana', 'orange', 'banana']) # True
has_duplicates([]) # False
```

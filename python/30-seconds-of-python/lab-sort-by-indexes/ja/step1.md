# インデックスに基づくリストのソート

2つのリストを引数として受け取り、2番目のリストのインデックスに基づいてソートされた新しいリストを返す関数`sort_by_indexes(lst, indexes, reverse=False)`を作成します。この関数は以下のパラメータを持つ必要があります。

- `lst`：ソート対象の要素のリスト。
- `indexes`：`lst`をソートするための目的のインデックスを表す整数のリスト。
- `reverse`：オプションのブール型パラメータで、`True`に設定すると、リストを逆順にソートします。

この関数は、2番目のリストのインデックスに基づいてソートされた新しいリストを返す必要があります。

```python
def sort_by_indexes(lst, indexes, reverse=False):
  return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: \
          x[0], reverse=reverse)]
```

```python
a = ['eggs', 'bread', 'oranges', 'jam', 'apples','milk']
b = [3, 2, 6, 4, 1, 5]
sort_by_indexes(a, b) # ['apples', 'bread', 'eggs', 'jam','milk', 'oranges']
sort_by_indexes(a, b, True)
# ['oranges','milk', 'jam', 'eggs', 'bread', 'apples']
```

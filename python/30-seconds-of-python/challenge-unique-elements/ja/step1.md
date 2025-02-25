# リスト内の一意の要素

## 問題

`unique_elements` という名前の Python 関数を書きます。この関数は、リストを入力として受け取り、一意の要素のみを含む新しいリストを返します。関数は次の手順を実行する必要があります。

- 重複する値を除外するために、リストから `set` を作成します。
- `set` から `list` を返します。

関数のシグネチャは次のようになります。

```python
def unique_elements(li: List) -> List:
```

## 例

```python
assert unique_elements([1, 2, 2, 3, 4, 3]) == [1, 2, 3, 4]
assert unique_elements(['a', 'b', 'c', 'a', 'd']) == ['a', 'b', 'c', 'd']
assert unique_elements([]) == []
```

# リストから辞書へ

2つのリストを入力として受け取り、最初のリストの要素をキーとし、2番目のリストの要素を値とする辞書を返す `to_dictionary(keys, values)` 関数を書きます。この関数は、2つのリストの値を辞書に結合するために `zip()` と `dict()` を組み合わせて使用する必要があります。2つのリストの長さが等しくない場合、関数は `None` を返す必要があります。

```python
def to_dictionary(keys, values):
  return dict(zip(keys, values))
```

```python
to_dictionary(['a', 'b'], [1, 2]) # { a: 1, b: 2 }
```

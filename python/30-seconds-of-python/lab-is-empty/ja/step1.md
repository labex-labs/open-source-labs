# コレクションが空かどうか

`is_empty(val)` という Python 関数を作成します。この関数は、値をパラメータとして受け取り、その値が空のシーケンスまたはコレクションであれば `True` を返し、そうでなければ `False` を返します。

シーケンスまたはコレクションが空かどうかを確認するには、提供されたシーケンスまたはコレクションの真偽値をテストするために `not` 演算子を使用できます。シーケンスまたはコレクションが空の場合、`not` 演算子は `True` を返します。

あなたの関数は、次の種類のシーケンスとコレクションを処理できる必要があります。

- リスト
- タプル
- セット
- 辞書
- 文字列
- レンジ

```python
def is_empty(val):
  return not val
```

```python
is_empty([]) # True
is_empty({}) # True
is_empty('') # True
is_empty(set()) # True
is_empty(range(0)) # True
is_empty([1, 2]) # False
is_empty({ 'a': 1, 'b': 2 }) # False
is_empty('text') # False
is_empty(set([1, 2])) # False
is_empty(range(2)) # False
```

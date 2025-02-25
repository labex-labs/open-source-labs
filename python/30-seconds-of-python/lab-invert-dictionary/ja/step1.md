# 辞書を逆転させる

`invert_dictionary(obj)` というPython関数を書きます。この関数は、辞書 `obj` を引数として受け取り、キーと値を逆転させた新しい辞書を返します。入力辞書 `obj` は一意のハッシュ可能な値を持つものとします。出力辞書は、入力辞書と同じキーを持つようにしますが、値は入力辞書のキーになります。

新しい辞書を作成するために、`dictionary.items()` をリスト内包表記と組み合わせて使用する必要があります。

```python
def invert_dictionary(obj):
  return { value: key for key, value in obj.items() }
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: 'Peter', 11: 'Isabel', 9: 'Anna' }
```

# 辞書を反転させる

## 問題

辞書 `obj` を入力として受け取り、キーと値を反転させた新しい辞書を返す関数 `invert_dictionary(obj)` を書きます。入力辞書は、非一意のハッシュ可能な値を持ちます。2 つ以上のキーが同じ値を持つ場合、関数は出力辞書のリストにキーを追加する必要があります。

この問題を解決するには、次の手順をたどることができます。

1. 各キーの既定値として `list` を持つ `collections.defaultdict` を作成します。
2. `dictionary.items()` をループと組み合わせて、`dict.append()` を使用して辞書の値をキーにマッピングします。
3. `dict()` を使用して、`collections.defaultdict` を通常の辞書に変換します。

関数のシグネチャ：`def invert_dictionary(obj: dict) -> dict:`

## 例

```python
ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }
```

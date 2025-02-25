# 辞書を反転させる

`invert_dictionary(obj)` という関数を書きましょう。この関数は、辞書 `obj` を入力として受け取り、キーと値を反転させた新しい辞書を返します。入力となる辞書は、非一意のハッシュ可能な値を持っています。2つ以上のキーが同じ値を持つ場合、関数は出力辞書のリストにキーを追加する必要があります。

この問題を解決するには、次の手順を辿ることができます。

1. 各キーの既定値として `list` を持つ `collections.defaultdict` を作成します。
2. `dictionary.items()` をループと組み合わせて、`dict.append()` を使って辞書の値をキーにマッピングします。
3. `dict()` を使って、`collections.defaultdict` を通常の辞書に変換します。

関数のシグネチャ: `def invert_dictionary(obj: dict) -> dict:`

```python
from collections import defaultdict

def collect_dictionary(obj):
  inv_obj = defaultdict(list)
  for key, value in obj.items():
    inv_obj[value].append(key)
  return dict(inv_obj)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}
collect_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }
```

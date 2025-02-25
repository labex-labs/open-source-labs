# 辞書の値を結合する

2つ以上の辞書を引数として受け取り、入力辞書の値を結合した新しい辞書を返す関数`combine_values(*dicts)`を作成します。この関数は次の手順を実行する必要があります。

1. 新しい`collections.defaultdict`を作成し、各キーの既定値として`list`を使用します。
2. 入力辞書をループし、各辞書に対して：
   - 辞書のキーをループします。
   - キーの値を`defaultdict`のそのキーの値のリストに追加します。
3. `defaultdict`を`dict()`関数を使用して通常の辞書に変換します。
4. 結果の辞書を返します。

この関数は次のシグネチャを持つ必要があります。

```python
def combine_values(*dicts):
    pass
```

```python
from collections import defaultdict

def combine_values(*dicts):
  res = defaultdict(list)
  for d in dicts:
    for key in d:
      res[key].append(d[key])
  return dict(res)
```

```python
d1 = {'a': 1, 'b': 'foo', 'c': 400}
d2 = {'a': 3, 'b': 200, 'd': 400}

combine_values(d1, d2) # {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}
```

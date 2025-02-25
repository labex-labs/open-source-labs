# リスト要素をグループ化する

引数としてリスト `lst` と関数 `fn` を受け取り、`fn` を `lst` の要素に適用した結果をキーとし、`fn` をそれらに適用したときに対応するキーを生成する `lst` の要素のリストを値とする辞書を返す関数 `group_by(lst, fn)` を書きなさい。

たとえば、数値のリスト `[6.1, 4.2, 6.3]` があり、それらを整数部分でグループ化したい場合、グループ化関数として `math` モジュールの `floor` 関数を使用できます。期待される出力は `{4: [4.2], 6: [6.1, 6.3]}` になります。

```python
from collections import defaultdict

def group_by(lst, fn):
  d = defaultdict(list)
  for el in lst:
    d[fn(el)].append(el)
  return dict(d)
```

```python
from math import floor

group_by([6.1, 4.2, 6.3], floor) # {4: [4.2], 6: [6.1, 6.3]}
group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}
```

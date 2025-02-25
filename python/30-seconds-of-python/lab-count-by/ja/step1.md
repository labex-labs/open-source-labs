# グループ化された要素のカウント

引数としてリスト `lst` と関数 `fn` を受け取る関数 `count_by(lst, fn = lambda x: x)` を書きます。この関数は、与えられた関数に基づいてリストの要素をグループ化し、各グループの要素数を含む辞書を返す必要があります。

この問題を解決するには、次の手順を辿ることができます。

1. `collections.defaultdict` を使用して辞書を初期化します。
2. `map()` を使用して与えられた関数をリストの各要素に適用します。
3. マッピングされた値を反復処理し、辞書内の各要素のカウントを増やします。

関数は結果の辞書を返す必要があります。

```python
from collections import defaultdict

def count_by(lst, fn = lambda x: x):
  count = defaultdict(int)
  for val in map(fn, lst):
    count[val] += 1
  return dict(count)
```

```python
from math import floor

count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}
```

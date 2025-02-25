# 値の頻度

引数としてリストを受け取り、そのリストの一意の値をキーとし、それらの頻度を値とする辞書を返す、`value_frequencies(lst)` という名前のPython関数を作成します。

この問題を解くには、次の手順に従うことができます。

1. 各一意の要素の頻度を格納するための空の辞書を作成します。
2. リストをループして、`collections.defaultdict` を使って各一意の要素の頻度を格納します。
3. `dict()` を使って、リストの一意の要素をキーとし、それらの頻度を値とする辞書を返します。

あなたの関数は、一意の値とそれらの頻度を持つ辞書を返す必要があります。

```python
from collections import defaultdict

def frequencies(lst):
  freq = defaultdict(int)
  for val in lst:
    freq[val] += 1
  return dict(freq)
```

```python
frequencies(['a', 'b', 'a', 'c', 'a', 'a', 'b']) # { 'a': 4, 'b': 2, 'c': 1 }
```

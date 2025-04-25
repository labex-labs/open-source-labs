# 文字列のアナグラム

2 つの文字列を引数として受け取り、それらが互いにアナグラムであれば `True` を返し、そうでなければ `False` を返す関数 `is_anagram(s1, s2)` を書きます。この関数は大文字小文字を区別せず、空白、句読点、特殊文字を無視する必要があります。

この問題を解くには、次の手順を辿ることができます。

1. `str.isalnum()` を使って半角英数字以外の文字をフィルタリングし、`str.lower()` を使って各文字を小文字に変換します。
2. `collections.Counter` を使って各文字列の結果となる文字を数え、結果を比較します。

```python
from collections import Counter

def is_anagram(s1, s2):
  return Counter(
    c.lower() for c in s1 if c.isalnum()
  ) == Counter(
    c.lower() for c in s2 if c.isalnum()
  )
```

```python
is_anagram('#anagram', 'Nag a ram!')  # True
```

# 前処理関数の定義

トークンは、単語、単語の一部、または文字列内の空白や記号の間に含まれる何かです。ここでは、単純な正規表現（regex）を使用してトークンを抽出する関数を定義します。この正規表現は、Unicodeの単語文字と一致します。これには、あらゆる言語の単語の一部となり得るほとんどの文字、および数字とアンダースコアが含まれます。

```python
import re

def tokenize(doc):
    """Extract tokens from doc.

    This uses a simple regex that matches word characters to break strings
    into tokens. For a more principled approach, see CountVectorizer or
    TfidfVectorizer.
    """
    return (tok.lower() for tok in re.findall(r"\w+", doc))
```

与えられた文書内の各トークンの出現回数（頻度）をカウントする追加の関数を定義します。ベクトル化関数によって使用される頻度辞書を返します。

```python
from collections import defaultdict

def token_freqs(doc):
    """Extract a dict mapping tokens from doc to their occurrences."""

    freq = defaultdict(int)
    for tok in tokenize(doc):
        freq[tok] += 1
    return freq
```

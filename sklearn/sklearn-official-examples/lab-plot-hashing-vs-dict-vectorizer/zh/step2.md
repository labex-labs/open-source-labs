# 定义预处理函数

一个词元可以是一个单词、单词的一部分，或者是字符串中两个空格或符号之间的任何内容。在这里，我们定义一个函数，该函数使用一个简单的正则表达式（regex）来提取词元，该正则表达式匹配Unicode单词字符。这包括任何语言中可能作为单词一部分的大多数字符，以及数字和下划线：

```python
import re

def tokenize(doc):
    """从文档中提取词元。

    这使用一个简单的正则表达式来匹配单词字符，从而将字符串拆分为词元。
    若要采用更有原则的方法，请参阅CountVectorizer或TfidfVectorizer。
    """
    return (tok.lower() for tok in re.findall(r"\w+", doc))
```

我们定义另一个函数，该函数统计给定文档中每个词元的（出现频率）。它返回一个频率字典，供向量化器使用。

```python
from collections import defaultdict

def token_freqs(doc):
    """提取一个字典，将文档中的词元映射到它们的出现次数。"""

    freq = defaultdict(int)
    for tok in tokenize(doc):
        freq[tok] += 1
    return freq
```

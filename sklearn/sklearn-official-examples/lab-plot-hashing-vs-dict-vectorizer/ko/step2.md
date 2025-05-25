# 전처리 함수 정의

토큰은 단어, 단어 일부 또는 문자열에서 공백이나 기호 사이에 포함된 모든 것을 의미할 수 있습니다. 여기서는 유니코드 단어 문자를 일치시키는 간단한 정규 표현식 (regex) 을 사용하여 토큰을 추출하는 함수를 정의합니다. 이에는 모든 언어에서 단어의 일부가 될 수 있는 대부분의 문자와 숫자, 밑줄이 포함됩니다.

```python
import re

def tokenize(doc):
    """doc 에서 토큰을 추출합니다.

    문자열을 토큰으로 분할하기 위해 단어 문자를 일치시키는 간단한 정규 표현식을 사용합니다.
    더 체계적인 접근 방식은 CountVectorizer 또는 TfidfVectorizer 를 참조하십시오.
    """
    return (tok.lower() for tok in re.findall(r"\w+", doc))
```

주어진 문서에서 각 토큰의 발생 빈도를 계산하는 추가 함수를 정의합니다. 벡터화기에 사용할 빈도 사전을 반환합니다.

```python
from collections import defaultdict

def token_freqs(doc):
    """doc 에서 토큰과 그 발생 횟수를 매핑하는 사전을 추출합니다."""

    freq = defaultdict(int)
    for tok in tokenize(doc):
        freq[tok] += 1
    return freq
```

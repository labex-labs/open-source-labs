# NumberNormalizingVectorizer 정의

이전에 정의한 `number_normalizer()` 함수를 사용하는 토크나이저를 구축하기 위해 `TfidfVectorizer()`를 상속하는 `NumberNormalizingVectorizer()` 클래스를 정의합니다.

```python
class NumberNormalizingVectorizer(TfidfVectorizer):
    def build_tokenizer(self):
        tokenize = super().build_tokenizer()
        return lambda doc: list(number_normalizer(tokenize(doc)))
```

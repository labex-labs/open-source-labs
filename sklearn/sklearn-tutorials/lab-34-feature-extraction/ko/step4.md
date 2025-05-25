# 벡터라이저 클래스 사용자 지정

이 단계에서는 호출 가능한 함수를 벡터라이저 클래스에 전달하여 그 동작을 사용자 지정하는 방법을 배웁니다.

```python
def my_tokenizer(s):
    return s.split()

vectorizer = CountVectorizer(tokenizer=my_tokenizer)
features = vectorizer.fit_transform(corpus).toarray()

print(features)
```

# 텍스트 특징 추출

이 단계에서는 scikit-learn 의 `CountVectorizer` 및 `TfidfVectorizer` 클래스를 사용하여 텍스트 특징 추출을 수행하는 방법을 배웁니다. 이러한 클래스는 텍스트 데이터를 수치 특징으로 변환하는 데 사용될 수 있습니다.

```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]

vectorizer = CountVectorizer()
features = vectorizer.fit_transform(corpus).toarray()
feature_names = vectorizer.get_feature_names_out()

print(features)
print(feature_names)
```

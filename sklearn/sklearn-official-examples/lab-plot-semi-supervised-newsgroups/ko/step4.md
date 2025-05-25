# 자기지도 학습 파이프라인 생성

이 단계에서는 자기지도 학습을 위한 파이프라인을 생성합니다. 이 파이프라인은 지도 학습 파이프라인과 유사하지만, SGDClassifier 대신 SelfTrainingClassifier 를 사용합니다.

```python
from sklearn.semi_supervised import SelfTrainingClassifier

# 자기지도 학습 파이프라인 생성
st_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SelfTrainingClassifier(SGDClassifier(**sdg_params), verbose=True)),
    ]
)
```

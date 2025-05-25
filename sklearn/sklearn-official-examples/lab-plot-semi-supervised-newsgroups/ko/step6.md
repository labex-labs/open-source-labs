# LabelSpreading 파이프라인 생성

이 단계에서는 LabelSpreading 을 사용한 준지도 학습을 위한 파이프라인을 생성합니다. 이 파이프라인은 지도 학습 파이프라인과 유사하지만, SGDClassifier 대신 LabelSpreading 알고리즘을 사용합니다.

```python
from sklearn.semi_supervised import LabelSpreading
from sklearn.preprocessing import FunctionTransformer

# LabelSpreading 파이프라인 생성
ls_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("toarray", FunctionTransformer(lambda x: x.toarray())),
        ("clf", LabelSpreading()),
    ]
)
```

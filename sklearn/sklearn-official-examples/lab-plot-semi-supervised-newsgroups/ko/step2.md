# 지도 학습 파이프라인 생성

이 단계에서는 지도 학습을 위한 파이프라인을 생성합니다. 파이프라인은 텍스트 데이터를 토큰 빈도 행렬로 변환하는 CountVectorizer, 카운트 행렬에 역문서 빈도 정규화 (TF-IDF) 를 적용하는 TfidfTransformer, 그리고 모델을 학습하는 SGDClassifier 로 구성됩니다.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# SGDClassifier 의 매개변수
sdg_params = dict(alpha=1e-5, penalty="l2", loss="log_loss")

# CountVectorizer 의 매개변수
vectorizer_params = dict(ngram_range=(1, 2), min_df=5, max_df=0.8)

# 파이프라인 생성
pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SGDClassifier(**sdg_params)),
    ]
)
```

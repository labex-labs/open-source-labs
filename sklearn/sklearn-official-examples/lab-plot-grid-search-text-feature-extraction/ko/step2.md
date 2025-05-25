# 하이퍼파라미터 튜닝을 사용한 파이프라인 정의

텍스트 분류를 위해 텍스트 특징 벡터화기와 간단한 분류기를 결합한 파이프라인을 정의합니다. Complement Naive Bayes 를 분류기로, TfidfVectorizer 를 특징 추출기로 사용합니다.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import ComplementNB
from sklearn.pipeline import Pipeline
import numpy as np

pipeline = Pipeline(
    [
        ("vect", TfidfVectorizer()),
        ("clf", ComplementNB()),
    ]
)

parameter_grid = {
    "vect__max_df": (0.2, 0.4, 0.6, 0.8, 1.0),
    "vect__min_df": (1, 3, 5, 10),
    "vect__ngram_range": ((1, 1), (1, 2)),  # unigrams or bigrams
    "vect__norm": ("l1", "l2"),
    "clf__alpha": np.logspace(-6, 6, 13),
}
```

# 텍스트 데이터 전처리

머신러닝에 텍스트 데이터를 사용하기 전에 전처리가 필요합니다. 이는 구두점 제거, 모든 텍스트를 소문자로 변환, 텍스트를 개별 단어로 토큰화하는 등 여러 단계를 포함합니다. scikit-learn 의 `CountVectorizer`와 `TfidfTransformer`를 사용하여 이러한 전처리 단계를 수행할 수 있습니다.

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# 텍스트 데이터 전처리
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
```

이제 텍스트 데이터가 전처리되어 특징 추출 준비가 완료되었습니다.

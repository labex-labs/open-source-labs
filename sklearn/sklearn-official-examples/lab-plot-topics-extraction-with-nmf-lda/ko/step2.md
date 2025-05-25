# 특징 추출

NMF 에는 tf-idf 특징을, LDA 에는 원시 단어 빈도 특징을 사용하여 데이터셋에서 특징을 추출합니다.

```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# NMF 를 위해 tf-idf 특징 사용.
print("NMF 를 위한 tf-idf 특징 추출 중...")
tfidf_vectorizer = TfidfVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tfidf = tfidf_vectorizer.fit_transform(data_samples)

# LDA 를 위해 원시 단어 빈도 특징 사용.
print("LDA 를 위한 tf 특징 추출 중...")
tf_vectorizer = CountVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tf = tf_vectorizer.fit_transform(data_samples)
```

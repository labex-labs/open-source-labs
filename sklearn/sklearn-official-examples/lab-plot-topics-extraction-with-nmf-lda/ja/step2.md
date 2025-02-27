# 特徴量の抽出

NMF のために tf-idf 特徴量と、LDA のために単語出現回数の特徴量を使って、データセットから特徴量を抽出します。

```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# NMF のために tf-idf 特徴量を使用します。
print("Extracting tf-idf features for NMF...")
tfidf_vectorizer = TfidfVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tfidf = tfidf_vectorizer.fit_transform(data_samples)

# LDA のために単語出現回数の特徴量を使用します。
print("Extracting tf features for LDA...")
tf_vectorizer = CountVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tf = tf_vectorizer.fit_transform(data_samples)
```

# Extraer Características

Extraeremos las características del conjunto de datos utilizando características tf-idf para NMF y características de recuento de términos brutos para LDA.

```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# Utilizar características tf-idf para NMF.
print("Extracting tf-idf features for NMF...")
tfidf_vectorizer = TfidfVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tfidf = tfidf_vectorizer.fit_transform(data_samples)

# Utilizar características de recuento de términos brutos para LDA.
print("Extracting tf features for LDA...")
tf_vectorizer = CountVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tf = tf_vectorizer.fit_transform(data_samples)
```

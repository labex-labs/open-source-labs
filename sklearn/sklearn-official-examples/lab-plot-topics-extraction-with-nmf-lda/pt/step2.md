# Extrair Recursos

Extrairemos recursos do conjunto de dados usando recursos tf-idf para NMF e recursos de contagem de termos brutos para LDA.

```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# Use recursos tf-idf para NMF.
print("Extraindo recursos tf-idf para NMF...")
tfidf_vectorizer = TfidfVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tfidf = tfidf_vectorizer.fit_transform(data_samples)

# Use recursos de contagem de termos brutos para LDA.
print("Extraindo recursos tf para LDA...")
tf_vectorizer = CountVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tf = tf_vectorizer.fit_transform(data_samples)
```

# Извлечение признаков

Мы будем извлекать признаки из датасета, используя tf-idf признаки для NMF и признаки подсчета исходных терминов для LDA.

```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# Используем tf-idf признаки для NMF.
print("Extracting tf-idf features for NMF...")
tfidf_vectorizer = TfidfVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tfidf = tfidf_vectorizer.fit_transform(data_samples)

# Используем признаки подсчета исходных терминов для LDA.
print("Extracting tf features for LDA...")
tf_vectorizer = CountVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tf = tf_vectorizer.fit_transform(data_samples)
```

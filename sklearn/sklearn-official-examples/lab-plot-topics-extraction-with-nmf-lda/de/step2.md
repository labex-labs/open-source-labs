# Extrahiere Merkmale

Wir werden Merkmale aus dem Datensatz extrahieren, indem wir tf-idf-Merkmale für die NMF und einfache Termzähler-Merkmale für die LDA verwenden.

```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# Verwende tf-idf-Merkmale für die NMF.
print("Extrahiere tf-idf-Merkmale für die NMF...")
tfidf_vectorizer = TfidfVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tfidf = tfidf_vectorizer.fit_transform(data_samples)

# Verwende einfache Termzähler-Merkmale für die LDA.
print("Extrahiere tf-Merkmale für die LDA...")
tf_vectorizer = CountVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tf = tf_vectorizer.fit_transform(data_samples)
```

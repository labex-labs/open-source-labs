# Extraire les caractéristiques

Nous allons extraire les caractéristiques à partir du jeu de données en utilisant les caractéristiques tf-idf pour la NMF et les comptes de termes bruts pour la LDA.

```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# Utiliser les caractéristiques tf-idf pour la NMF.
print("Extraction des caractéristiques tf-idf pour la NMF...")
tfidf_vectorizer = TfidfVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tfidf = tfidf_vectorizer.fit_transform(data_samples)

# Utiliser les caractéristiques de comptage de termes bruts pour la LDA.
print("Extraction des caractéristiques tf pour la LDA...")
tf_vectorizer = CountVectorizer(
    max_df=0.95, min_df=2, max_features=n_features, stop_words="english"
)
tf = tf_vectorizer.fit_transform(data_samples)
```

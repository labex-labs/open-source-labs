# Extraction de caractéristiques de texte

Dans cette étape, nous allons apprendre à effectuer l'extraction de caractéristiques de texte à l'aide des classes `CountVectorizer` et `TfidfVectorizer` dans scikit-learn. Ces classes peuvent être utilisées pour convertir les données textuelles en caractéristiques numériques.

```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]

vectorizer = CountVectorizer()
features = vectorizer.fit_transform(corpus).toarray()
feature_names = vectorizer.get_feature_names_out()

print(features)
print(feature_names)
```

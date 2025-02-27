# Extracción de características de texto

En este paso, aprenderemos a realizar la extracción de características de texto utilizando las clases `CountVectorizer` y `TfidfVectorizer` en scikit-learn. Estas clases se pueden utilizar para convertir datos de texto en características numéricas.

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

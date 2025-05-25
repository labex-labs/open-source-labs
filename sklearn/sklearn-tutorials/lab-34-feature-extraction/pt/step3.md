# Extração de Características de Texto

Neste passo, aprenderemos a realizar a extração de características de texto utilizando as classes `CountVectorizer` e `TfidfVectorizer` na biblioteca scikit-learn. Estas classes podem ser usadas para converter dados de texto em características numéricas.

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

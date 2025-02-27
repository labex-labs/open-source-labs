# Text-Feature-Extraktion

In diesem Schritt werden wir lernen, wie man die Text-Feature-Extraktion mit den Klassen `CountVectorizer` und `TfidfVectorizer` in scikit-learn durchführt. Diese Klassen können verwendet werden, um Text-Daten in numerische Features umzuwandeln.

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

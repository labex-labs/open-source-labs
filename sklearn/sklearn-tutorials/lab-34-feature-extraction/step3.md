# Text feature extraction

In this step, we will learn how to perform text feature extraction using the `CountVectorizer` and `TfidfVectorizer` classes in scikit-learn. These classes can be used to convert text data into numerical features.

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

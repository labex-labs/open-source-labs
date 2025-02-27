# Извлечение текстовых признаков

В этом шаге мы научимся выполнять извлечение текстовых признаков с использованием классов `CountVectorizer` и `TfidfVectorizer` в scikit-learn. Эти классы можно использовать для преобразования текстовых данных в числовые признаки.

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

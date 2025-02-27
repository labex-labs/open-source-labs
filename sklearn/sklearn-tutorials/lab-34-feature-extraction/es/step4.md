# Personalización de las clases vectorizadoras

En este paso, aprenderemos a personalizar el comportamiento de las clases vectorizadoras al pasarles funciones llamables.

```python
def my_tokenizer(s):
    return s.split()

vectorizer = CountVectorizer(tokenizer=my_tokenizer)
features = vectorizer.fit_transform(corpus).toarray()

print(features)
```

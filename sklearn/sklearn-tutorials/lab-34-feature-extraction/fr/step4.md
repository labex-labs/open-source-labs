# Personnalisation des classes de vectorisation

Dans cette étape, nous allons apprendre à personnaliser le comportement des classes de vectorisation en leur passant des fonctions appelables.

```python
def my_tokenizer(s):
    return s.split()

vectorizer = CountVectorizer(tokenizer=my_tokenizer)
features = vectorizer.fit_transform(corpus).toarray()

print(features)
```

# Настройка классов векторизаторов

В этом шаге мы научимся настраивать поведение классов векторизаторов, передавая им вызываемые функции.

```python
def my_tokenizer(s):
    return s.split()

vectorizer = CountVectorizer(tokenizer=my_tokenizer)
features = vectorizer.fit_transform(corpus).toarray()

print(features)
```

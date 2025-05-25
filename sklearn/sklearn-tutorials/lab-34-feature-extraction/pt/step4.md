# Personalizando as classes de vetorização

Neste passo, aprenderemos como personalizar o comportamento das classes de vetorização passando funções executáveis para elas.

```python
def my_tokenizer(s):
    return s.split()

vectorizer = CountVectorizer(tokenizer=my_tokenizer)
features = vectorizer.fit_transform(corpus).toarray()

print(features)
```

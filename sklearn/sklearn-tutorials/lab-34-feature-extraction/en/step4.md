# Customizing the vectorizer classes

In this step, we will learn how to customize the behavior of vectorizer classes by passing callable functions to them.

```python
def my_tokenizer(s):
    return s.split()

vectorizer = CountVectorizer(tokenizer=my_tokenizer)
features = vectorizer.fit_transform(corpus).toarray()

print(features)
```

# Anpassen der Vektorizer-Klassen

In diesem Schritt werden wir lernen, wie man das Verhalten von Vektorizer-Klassen anpasst, indem man aufrufbar Funktionen an sie übergibt.

```python
def my_tokenizer(s):
    return s.split()

vectorizer = CountVectorizer(tokenizer=my_tokenizer)
features = vectorizer.fit_transform(corpus).toarray()

print(features)
```

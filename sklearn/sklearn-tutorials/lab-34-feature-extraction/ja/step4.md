# ベクトル化クラスのカスタマイズ

このステップでは、ベクトル化クラスに呼び出し可能な関数を渡すことで、それらの動作をカスタマイズする方法を学びます。

```python
def my_tokenizer(s):
    return s.split()

vectorizer = CountVectorizer(tokenizer=my_tokenizer)
features = vectorizer.fit_transform(corpus).toarray()

print(features)
```

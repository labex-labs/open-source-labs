# 自定义向量化器类

在这一步中，我们将学习如何通过向向量化器类传递可调用函数来定制它们的行为。

```python
def my_tokenizer(s):
    return s.split()

vectorizer = CountVectorizer(tokenizer=my_tokenizer)
features = vectorizer.fit_transform(corpus).toarray()

print(features)
```

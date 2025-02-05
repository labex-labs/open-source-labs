# 文本特征提取

在这一步中，我们将学习如何使用scikit-learn中的`CountVectorizer`和`TfidfVectorizer`类来执行文本特征提取。这些类可用于将文本数据转换为数值特征。

```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?'
]

vectorizer = CountVectorizer()
features = vectorizer.fit_transform(corpus).toarray()
feature_names = vectorizer.get_feature_names_out()

print(features)
print(feature_names)
```

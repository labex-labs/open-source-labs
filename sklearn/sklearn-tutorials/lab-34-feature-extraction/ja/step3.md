# テキスト特徴抽出

このステップでは、scikit-learnの`CountVectorizer`と`TfidfVectorizer`クラスを使ってテキスト特徴抽出を行う方法を学びます。これらのクラスは、テキストデータを数値特徴に変換するために使用できます。

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

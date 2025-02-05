# 预处理文本数据

在我们将文本数据用于机器学习之前，需要对其进行预处理。这涉及几个步骤，例如去除标点符号、将所有文本转换为小写，以及将文本分词为单个单词。我们可以使用scikit-learn的`CountVectorizer`和`TfidfTransformer`来执行这些预处理步骤。

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# 预处理文本数据
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
```

现在我们的文本数据已经过预处理，可以进行特征提取了。

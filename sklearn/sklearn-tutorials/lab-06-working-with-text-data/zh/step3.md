# 特征提取

为了将文本数据表示为特征向量，我们可以使用词袋表示法。这种表示法为训练集中的每个单词分配一个固定的整数 ID，并统计每个单词在每个文档中的出现次数。我们可以使用 scikit-learn 的`CountVectorizer`来提取这些特征向量。

```python
from sklearn.feature_extraction.text import CountVectorizer

# 提取特征向量
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
```

现在我们已经提取了特征向量，可以将它们用于训练我们的模型。

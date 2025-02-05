# 训练模型

既然我们已经有了特征向量，就可以训练一个模型来对文本数据进行分类。在这个例子中，我们将使用多项式朴素贝叶斯算法，这是一种用于文本分类的流行算法。

```python
from sklearn.naive_bayes import MultinomialNB

# 训练模型
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
```

现在我们的模型已经训练好，可以进行预测了。

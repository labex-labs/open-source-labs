# 在变换后的数据上学习朴素贝叶斯分类器

在这一步中，我们将在变换后的数据上学习一个朴素贝叶斯分类器。

```python
nb = BernoulliNB()
nb.fit(X_transformed, y)
```

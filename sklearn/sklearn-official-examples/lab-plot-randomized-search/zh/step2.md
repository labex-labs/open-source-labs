# 创建一个支持向量机模型

我们将创建一个采用随机梯度下降（SGD）训练的线性支持向量机模型。

```python
# create SVM model with SGD training
clf = SGDClassifier(loss="hinge", penalty="elasticnet", fit_intercept=True)
```

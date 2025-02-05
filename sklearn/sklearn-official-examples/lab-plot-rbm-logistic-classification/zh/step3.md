# 训练

在这一步中，我们训练上一步定义的管道模型。我们设置模型的超参数（学习率、隐藏层大小、正则化），然后将训练数据拟合到模型中。

```python
from sklearn.base import clone

# 超参数。这些是通过交叉验证设置的，
# 使用GridSearchCV。这里为了节省时间我们不进行交叉验证。
rbm.learning_rate = 0.06
rbm.n_iter = 10

# 更多的组件往往会带来更好的预测性能，但拟合时间会更长
rbm.n_components = 100
logistic.C = 6000

# 训练RBM-逻辑回归管道
rbm_features_classifier.fit(X_train, Y_train)
```

# 模型定义

在这一步中，我们使用伯努利受限玻尔兹曼机（BernoulliRBM）特征提取器和逻辑回归分类器来定义分类管道。我们分别使用`sklearn.neural_network`和`sklearn.linear_model`模块中的`BernoulliRBM`和`LogisticRegression`类。然后，我们创建一个管道对象`rbm_features_classifier`来组合这两个模型。

```python
from sklearn import linear_model
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline

logistic = linear_model.LogisticRegression(solver="newton-cg", tol=1)
rbm = BernoulliRBM(random_state=0, verbose=True)

rbm_features_classifier = Pipeline(steps=[("rbm", rbm), ("logistic", logistic)])
```

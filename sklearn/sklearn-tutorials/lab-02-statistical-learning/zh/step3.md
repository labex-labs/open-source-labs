# 估计器对象

scikit-learn 中的估计器对象用于从数据中学习并进行预测。它们可以是分类、回归或聚类算法，也可以是从原始数据中提取有用特征的变换器。让我们创建一个估计器对象的简单示例：

```python
from sklearn.base import BaseEstimator

class Estimator(BaseEstimator):
    def __init__(self, param1=0, param2=0):
        self.param1 = param1
        self.param2 = param2

    def fit(self, data):
        # 拟合方法的实现
        pass

estimator = Estimator()
```

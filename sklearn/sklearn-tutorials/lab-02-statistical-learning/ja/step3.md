# 推定器オブジェクト

scikit-learn の推定器オブジェクトは、データから学習して予測を行うために使用されます。分類、回帰、クラスタリングアルゴリズム、または生データから有用な特徴量を抽出する変換器にすることができます。推定器オブジェクトの簡単な例を作成しましょう。

```python
from sklearn.base import BaseEstimator

class Estimator(BaseEstimator):
    def __init__(self, param1=0, param2=0):
        self.param1 = param1
        self.param2 = param2

    def fit(self, data):
        # Implementation of the fit method
        pass

estimator = Estimator()
```

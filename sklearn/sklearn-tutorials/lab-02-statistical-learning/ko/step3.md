# 추정기 객체

Scikit-learn 의 추정기 객체는 데이터로부터 학습하고 예측을 수행하는 데 사용됩니다. 분류, 회귀, 군집화 알고리즘, 또는 원시 데이터에서 유용한 특징을 추출하는 변환기일 수 있습니다. 추정기 객체의 간단한 예시를 만들어 보겠습니다.

```python
from sklearn.base import BaseEstimator

class Estimator(BaseEstimator):
    def __init__(self, param1=0, param2=0):
        self.param1 = param1
        self.param2 = param2

    def fit(self, data):
        # fit 메서드의 구현
        pass

estimator = Estimator()
```

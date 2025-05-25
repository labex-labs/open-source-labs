# Objetos Estimator

Objetos Estimator no scikit-learn são usados para aprender com dados e fazer previsões. Eles podem ser algoritmos de classificação, regressão ou agrupamento, ou transformadores que extraem recursos úteis de dados brutos. Vamos criar um exemplo simples de um objeto estimator:

```python
from sklearn.base import BaseEstimator

class Estimator(BaseEstimator):
    def __init__(self, param1=0, param2=0):
        self.param1 = param1
        self.param2 = param2

    def fit(self, data):
        # Implementação do método fit
        pass

estimator = Estimator()
```

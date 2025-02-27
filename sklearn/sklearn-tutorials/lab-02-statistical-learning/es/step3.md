# Objetos Estimadores

Los objetos estimadores en scikit-learn se utilizan para aprender a partir de datos y hacer predicciones. Pueden ser algoritmos de clasificación, regresión o agrupamiento, o transformadores que extraen características útiles de datos crudos. Veamos un ejemplo sencillo de un objeto estimador:

```python
from sklearn.base import BaseEstimator

class Estimator(BaseEstimator):
    def __init__(self, param1=0, param2=0):
        self.param1 = param1
        self.param2 = param2

    def fit(self, data):
        # Implementación del método fit
        pass

estimator = Estimator()
```

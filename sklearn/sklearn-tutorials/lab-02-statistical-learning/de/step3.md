# Schätzerobjekte

Schätzerobjekte in scikit-learn werden verwendet, um aus Daten zu lernen und Vorhersagen zu treffen. Sie können Klassifizierungs-, Regressions- oder Clustering-Algorithmen oder Transformatoren sein, die nützliche Merkmale aus Rohdaten extrahieren. Schauen wir uns ein einfaches Beispiel für ein Schätzerobjekt an:

```python
from sklearn.base import BaseEstimator

class Estimator(BaseEstimator):
    def __init__(self, param1=0, param2=0):
        self.param1 = param1
        self.param2 = param2

    def fit(self, data):
        # Implementation der fit-Methode
        pass

estimator = Estimator()
```

# Inicializar os Classificadores e o Conjunto de Dados

Primeiro, inicializaremos três classificadores e um conjunto de dados de exemplo. Usaremos `LogisticRegression`, `GaussianNB` e `RandomForestClassifier` como classificadores, e `X` e `y` como o conjunto de dados de exemplo.

```python
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier

clf1 = LogisticRegression(max_iter=1000, random_state=123)
clf2 = RandomForestClassifier(n_estimators=100, random_state=123)
clf3 = GaussianNB()
X = np.array([[-1.0, -1.0], [-1.2, -1.4], [-3.4, -2.2], [1.1, 1.2]])
y = np.array([1, 1, 2, 2])
```

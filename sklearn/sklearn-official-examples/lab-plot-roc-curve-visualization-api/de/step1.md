# Daten laden und einen SVC trainieren

Wir beginnen, indem wir den Weindatensatz laden und ihn in ein binäres Klassifizierungsproblem umwandeln. Anschließend werden wir einen Support-Vector-Klassifizierer auf dem Trainingsdatensatz trainieren.

```python
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import RocCurveDisplay
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

X, y = load_wine(return_X_y=True)
y = y == 2

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
svc = SVC(random_state=42)
svc.fit(X_train, y_train)
```

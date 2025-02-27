# Stichproben-Daten generieren

Wir werden Stichproben-Daten mit der Funktion `make_regression()` aus Scikit-learn generieren. Wir werden die Anzahl der Trainingsstichproben auf 75, die Anzahl der Teststichproben auf 150 und die Anzahl der Merkmale auf 500 setzen. Wir werden auch `n_informative` auf 50 und `shuffle` auf False setzen.

```python
import numpy as np
from sklearn import linear_model
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

n_samples_train, n_samples_test, n_features = 75, 150, 500
X, y, coef = make_regression(
    n_samples=n_samples_train + n_samples_test,
    n_features=n_features,
    n_informative=50,
    shuffle=False,
    noise=1.0,
    coef=True,
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=n_samples_train, test_size=n_samples_test, shuffle=False
)
```

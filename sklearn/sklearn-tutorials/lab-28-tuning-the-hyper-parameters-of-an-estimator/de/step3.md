# Definieren des Schätzers und des Parameterrahmens

Jetzt müssen wir den Schätzer definieren, den wir optimieren möchten, und den Parameterrahmen, in dem wir suchen möchten. Der Parameterrahmen gibt die Werte an, die wir für jeden Hyperparameter versuchen möchten.

```python
from sklearn.svm import SVC

# Erstelle eine Instanz des Support-Vector-Classifiers
svc = SVC()

# Definiere den Parameterrahmen
param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.1, 0.01, 0.001], 'kernel': ['linear', 'rbf']}
```

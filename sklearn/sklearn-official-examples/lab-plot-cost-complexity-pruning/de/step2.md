# Teilen der Daten

Wir werden die Daten in einen Trainingssatz und einen Testsatz aufteilen.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```

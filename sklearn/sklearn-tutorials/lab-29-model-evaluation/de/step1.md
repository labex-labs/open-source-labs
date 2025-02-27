# Estimator-Score-Methode

Die Estimator-Score-Methode ist ein standardmäßiges Bewertungsmaßstab, den scikit-learn für jeden Estimator zur Verfügung stellt. Sie berechnet einen Score, der die Qualität der Vorhersagen des Modells repräsentiert. Weitere Informationen hierzu finden Sie in der Dokumentation jedes Estimators.

Hier ist ein Beispiel für die Verwendung der `score`-Methode für einen Estimator:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()
clf.fit(X, y)

score = clf.score(X, y)
print("Score:", score)
```

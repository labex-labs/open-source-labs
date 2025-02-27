# Trainieren und Testen des Logistischen Regressionsmodells

Wir werden jetzt ein Logistisches Regressionsmodell mit der Funktion `LogisticRegression` von scikit-learn trainieren und es auf dem Testset testen. Anschließend werden wir die Genauigkeit des Modells ausgeben.

```python
from sklearn.linear_model import LogisticRegression

logistic = LogisticRegression(max_iter=1000)
logistic.fit(X_train, y_train)
logistic_score = logistic.score(X_test, y_test)

print("Logistic Regression score: %f" % logistic_score)
```

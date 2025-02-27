# Den Gauß'schen Naiven Bayes-Klassifizierer trainieren und evaluieren

Jetzt werden wir den Gauß'schen Naiven Bayes-Klassifizierer auf dem Trainingssatz trainieren und seine Leistung auf dem Testsatz evaluieren. Wir werden die Klasse `GaussianNB` aus dem Modul `sklearn.naive_bayes` verwenden.

```python
from sklearn.naive_bayes import GaussianNB

# Erstellen Sie einen Gauß'schen Naiven Bayes-Klassifizierer
gnb = GaussianNB()

# Trainieren Sie den Klassifizierer
gnb.fit(X_train, y_train)

# Vorhersagen Sie die Zielvariable für den Testsatz
y_pred = gnb.predict(X_test)

# Berechnen Sie die Genauigkeit des Klassifizierers
accuracy = (y_pred == y_test).sum() / len(y_test)
print("Genauigkeit:", accuracy)
```

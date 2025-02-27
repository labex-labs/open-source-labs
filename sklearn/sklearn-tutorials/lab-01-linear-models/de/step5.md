# Stochastic Gradient Descent (SGD)

Stochastic Gradient Descent (SGD) ist eine einfache, aber effiziente Methode zum Training von linearen Modellen. Es ist besonders nützlich, wenn die Anzahl der Samples und Merkmale sehr groß ist. SGD aktualisiert die Modellparameter bei jeder Iteration mit einem kleinen Teilsatz der Trainingsdaten, was es für das Online-Lernen und das Out-of-Core-Lernen geeignet macht.

Lassen Sie uns ein logistisches Regressionsmodell mit SGD anpassen.

```python
clf = linear_model.SGDClassifier(loss="log_loss", max_iter=1000)
clf.fit(X, y)

print(clf.coef_)
```

- Wir erstellen eine Instanz von `SGDClassifier` mit dem Parameter `loss` auf "log_loss" gesetzt, um logistische Regression durchzuführen.
- Wir verwenden die `fit`-Methode, um das Modell an die Trainingsdaten anzupassen.
- Wir drucken die Koeffizienten des logistischen Regressionsmodells, das mit SGD erhalten wurde.

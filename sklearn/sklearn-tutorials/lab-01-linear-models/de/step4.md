# Logistische Regression

Logistische Regression ist eine Klassifizierungsmethode, die die Wahrscheinlichkeiten der möglichen Ergebnisse mit einer logistischen Funktion abschätzt. Sie wird häufig für binäre Klassifizierungstasks verwendet. Logistische Regression kann auch erweitert werden, um multi - klasse Klassifizierungsprobleme zu behandeln.

Lassen Sie uns ein logistisches Regressionsmodell anpassen.

```python
clf = linear_model.LogisticRegression(random_state=0).fit(X, y)
print(clf.coef_)
```

- Wir erstellen eine Instanz von `LogisticRegression` mit dem Parameter `random_state` auf 0 gesetzt.
- Wir verwenden die `fit`-Methode, um das Modell an die Trainingsdaten anzupassen.
- Wir drucken die Koeffizienten des logistischen Regressionsmodells.

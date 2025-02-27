# Ein Bagging-Klassifizierer anpassen

Jetzt werden wir einen Bagging-Klassifizierer an den Trainingsdaten anpassen. Der Bagging-Klassifizierer ist ein Ensemble-Verfahren, das das Bootstrap-Sampling verwendet, um mehrere Basismodelle (oft Entscheidungsbäume) zu erstellen und deren Vorhersagen mithilfe der Mehrheitsentscheidung zu aggregieren.

```python
bagging = BaggingClassifier(DecisionTreeClassifier(), n_estimators=10)
bagging.fit(X_train, y_train)
```
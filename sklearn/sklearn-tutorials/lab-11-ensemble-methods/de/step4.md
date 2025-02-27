# Anpassen eines Bagging-Klassifikators

Jetzt werden wir einen Bagging-Klassifikator an die Trainingsdaten anpassen. Der Bagging-Klassifikator ist eine Ensemble-Methode, die Bootstrapping-Sampling verwendet, um mehrere Basismodelle (häufig Entscheidungsbäume) zu erstellen und deren Vorhersagen mithilfe der Mehrheitsentscheidung zusammenzufassen.

```python
bagging = BaggingClassifier(DecisionTreeClassifier(), n_estimators=10)
bagging.fit(X_train, y_train)
```

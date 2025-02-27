# Anpassen eines Random Forest-Klassifikators

Als Nächstes werden wir einen Random Forest-Klassifikator an die Trainingsdaten anpassen. Der Random Forest-Klassifikator ist ebenfalls eine Ensemble-Methode, die Bootstrapping-Sampling verwendet, um mehrere Entscheidungsbäume zu erstellen. Darüber hinaus fügt es zusätzliche Zufälligkeit hinzu, indem es bei jedem Split nur eine Teilmenge der Merkmale (Features) berücksichtigt.

```python
random_forest = RandomForestClassifier(n_estimators=10)
random_forest.fit(X_train, y_train)
```

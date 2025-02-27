# Ein Random Forest-Klassifizierer anpassen

Als nächstes werden wir einen Random Forest-Klassifizierer an den Trainingsdaten anpassen. Der Random Forest-Klassifizierer ist ebenfalls ein Ensemble-Verfahren, das das Bootstrap-Sampling verwendet, um mehrere Entscheidungsbäume zu erstellen, aber es fügt zusätzlich Zufälligkeit hinzu, indem bei jeder Aufteilung nur ein Teilmengen der Merkmale berücksichtigt wird.

```python
random_forest = RandomForestClassifier(n_estimators=10)
random_forest.fit(X_train, y_train)
```
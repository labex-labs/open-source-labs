# Anpassen des Klassifizierers

Nachdem der Datensatz erzeugt wurde, werden wir den Klassifizierer mit `LogisticRegression` aus scikit-learn anpassen.

```python
# Fit the classifier
clf = LogisticRegression(C=1e5)
clf.fit(X, y)
```

# Anpassen des isotonen Regressionsmodells

Jetzt können wir das isotone Regressionsmodell an unsere Daten anpassen. Wir erstellen eine Instanz der Klasse `IsotonicRegression` und rufen die `fit`-Methode mit unseren Eingabedaten und Zielwerten auf.

```python
# Fit isotonic regression model
ir = IsotonicRegression()
ir.fit(X, y)
```

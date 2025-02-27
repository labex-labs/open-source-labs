# Zeichnen Sie die Validierungskurve

Lassen Sie uns jetzt die Validierungskurve mit der Funktion `validation_curve` zeichnen. Wir werden den Schätzer `Ridge` verwenden und den Hyperparameter `alpha` über einen Bereich von Werten variieren.

```python
param_range = np.logspace(-7, 3, 3)
train_scores, valid_scores = validation_curve(
    Ridge(), X, y, param_name="alpha", param_range=param_range, cv=5)
```

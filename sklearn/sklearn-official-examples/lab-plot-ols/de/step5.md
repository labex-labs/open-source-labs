# Berechne Metriken

Wir können die Koeffizienten, den mittleren quadratischen Fehler und den Bestimmtheitskoeffizienten berechnen.

```python
from sklearn.metrics import mean_squared_error, r2_score

# Die Koeffizienten
print("Koeffizienten: \n", regr.coef_)

# Der mittlere quadratische Fehler
print("Mittlerer quadratischer Fehler: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))

# Der Bestimmtheitskoeffizient: 1 ist perfekte Vorhersage
print("Bestimmtheitskoeffizient: %.2f"
      % r2_score(diabetes_y_test, diabetes_y_pred))
```

# Berechnen der Validierungsergebnisse

Wir werden die `validation_curve`-Funktion aus scikit-learn verwenden, um die Trainings- und Validierungsergebnisse für den SVM-Klassifikator mit verschiedenen Werten von gamma zu berechnen.

```python
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

train_scores, test_scores = validation_curve(
    SVC(),
    X,
    y,
    param_name="gamma",
    param_range=param_range,
    scoring="accuracy",
    n_jobs=2,
)
```

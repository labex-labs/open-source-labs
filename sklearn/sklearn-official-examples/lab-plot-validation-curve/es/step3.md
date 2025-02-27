# Calculando las puntuaciones de validación

Usaremos la función `validation_curve` de scikit-learn para calcular las puntuaciones de entrenamiento y validación para el clasificador SVM con diferentes valores de gamma.

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

# Calcul des scores de validation

Nous allons utiliser la fonction `validation_curve` de scikit-learn pour calculer les scores d'entraînement et de validation pour le classifieur SVM avec différentes valeurs de gamma.

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

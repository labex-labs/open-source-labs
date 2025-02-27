# Entrenamiento y selección del modelo

Crearemos el objeto RFECV y computaremos las puntuaciones validadas cruzadas. La estrategia de puntuación "accuracy" (exactitud) optimiza la proporción de muestras clasificadas correctamente. Usaremos la regresión logística como estimador y la validación cruzada estratificada con 5 divisiones (folds).

```python
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression

min_features_to_select = 1  # Mínimo número de características a considerar
clf = LogisticRegression()
cv = StratifiedKFold(5)

rfecv = RFECV(
    estimator=clf,
    step=1,
    cv=cv,
    scoring="accuracy",
    min_features_to_select=min_features_to_select,
    n_jobs=2,
)
rfecv.fit(X, y)

print(f"Número óptimo de características: {rfecv.n_features_}")
```

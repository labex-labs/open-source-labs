# Validación cruzada no anidada

Utilizamos la validación cruzada no anidada para ajustar los hiperparámetros y evaluar el rendimiento del modelo. La función `GridSearchCV` realiza una búsqueda exhaustiva sobre los valores de parámetros especificados para un estimador. Utilizamos una validación cruzada de 4 pliegues (4-fold cross-validation).

```python
from sklearn.model_selection import GridSearchCV

# Non_nested parameter search and scoring
clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=4)
clf.fit(X_iris, y_iris)
non_nested_score = clf.best_score_
```

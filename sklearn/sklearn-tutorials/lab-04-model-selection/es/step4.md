# Estimadores validados cruzadamente

Algunos estimadores en scikit-learn tienen capacidades de validación cruzada integradas. Estos estimadores validados cruzadamente seleccionan automáticamente sus parámetros mediante validación cruzada, lo que hace que el proceso de selección de modelos sea más eficiente.

```python
from sklearn import linear_model, datasets

# Crear un objeto LassoCV
lasso = linear_model.LassoCV()

# Cargar el conjunto de datos de diabetes
X_diabetes, y_diabetes = datasets.load_diabetes(return_X_y=True)

# Ajustar el objeto LassoCV al conjunto de datos
lasso.fit(X_diabetes, y_diabetes)

print(lasso.alpha_)
```

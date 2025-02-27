# Búsqueda en cuadrícula

La búsqueda en cuadrícula es una técnica que se puede utilizar para encontrar la mejor combinación de valores de parámetros para un estimador. Consiste en especificar una cuadrícula de valores de parámetros, ajustar el estimador a los datos de entrenamiento para cada combinación de parámetros y seleccionar los parámetros que dan como resultado la puntuación de validación cruzada más alta.

```python
from sklearn.model_selection import GridSearchCV

# Definir una cuadrícula de valores de parámetros
Cs = np.logspace(-6, -1, 10)

# Crear un objeto GridSearchCV con el clasificador SVM y la cuadrícula de parámetros
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), n_jobs=-1)

# Ajustar el objeto GridSearchCV a los datos de entrenamiento
clf.fit(X_digits[:1000], y_digits[:1000])

print(clf.best_score_)
print(clf.best_estimator_.C)
```

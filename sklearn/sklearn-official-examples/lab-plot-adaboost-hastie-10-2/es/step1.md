# Preparar los datos y los modelos de referencia

Comenzamos generando el conjunto de datos de clasificación binaria utilizado en Hastie et al. 2009, Ejemplo 10.2. Luego, establecemos los hiperparámetros para nuestros clasificadores AdaBoost. Dividimos los datos en un conjunto de entrenamiento y un conjunto de prueba. Después de eso, entrenamos nuestros clasificadores de referencia, un `DecisionTreeClassifier` con `depth=9` y un `DecisionTreeClassifier` de "tronco" con `depth=1` y calculamos el error de prueba.

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = datasets.make_hastie_10_2(n_samples=12_000, random_state=1)

n_estimators = 400
learning_rate = 1.0

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=2_000, shuffle=False
)

dt_stump = DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)
dt_stump.fit(X_train, y_train)
dt_stump_err = 1.0 - dt_stump.score(X_test, y_test)

dt = DecisionTreeClassifier(max_depth=9, min_samples_leaf=1)
dt.fit(X_train, y_train)
dt_err = 1.0 - dt.score(X_test, y_test)
```

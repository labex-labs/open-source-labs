# Entrenar un clasificador de árbol de decisión

En primer lugar, necesitamos ajustar un clasificador de árbol de decisión utilizando el conjunto de datos `load_iris` de scikit-learn. Este conjunto de datos contiene 3 clases de 50 instancias cada una, donde cada clase se refiere a un tipo de planta de iris. Dividiremos el conjunto de datos en conjuntos de entrenamiento y prueba y ajustaremos un clasificador de árbol de decisión con un máximo de 3 nodos hoja.

```python
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

clf = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
clf.fit(X_train, y_train)
```

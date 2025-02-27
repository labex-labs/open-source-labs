# Mostrar la estructura del árbol de decisión

A continuación, mostraremos la estructura de un solo árbol de decisión entrenado con todas las características del conjunto de datos Iris.

```python
from sklearn.tree import plot_tree

plt.figure()
clf = DecisionTreeClassifier().fit(iris.data, iris.target)
plot_tree(clf, filled=True)
plt.title("Decision tree trained on all the iris features")
plt.show()
```

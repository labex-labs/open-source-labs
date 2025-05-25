# Treinar um Classificador de Árvore de Decisão

Primeiro, precisamos ajustar um classificador de árvore de decisão usando o conjunto de dados `load_iris` do scikit-learn. Este conjunto de dados contém 3 classes de 50 instâncias cada, onde cada classe se refere a um tipo de planta íris. Vamos dividir o conjunto de dados em conjuntos de treino e teste e ajustar um classificador de árvore de decisão com um máximo de 3 nós folha.

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

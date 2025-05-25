# Classificação por Vizinho Mais Próximo

Neste passo, exploraremos o conceito de classificação por vizinho mais próximo e como ele pode ser implementado usando o scikit-learn. Usaremos o conjunto de dados iris, que consiste em medições de diferentes flores de íris.

#### Carregar o Conjunto de Dados Iris

```python
import numpy as np
from sklearn import datasets

iris_X, iris_y = datasets.load_iris(return_X_y=True)
```

#### Dividir os Dados em Conjuntos de Treinamento e Teste

```python
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
```

#### Criar e Ajustar um Classificador de Vizinho Mais Próximo

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)
```

#### Fazer Predições

```python
predictions = knn.predict(iris_X_test)
```

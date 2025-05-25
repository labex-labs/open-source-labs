# Eliminação Recursiva de Características

A eliminação recursiva de características (RFE) é um método de seleção de características que considera recursivamente conjuntos menores e menores de características para selecionar as mais importantes. Funciona treinando um estimador externo com pesos atribuídos às características e eliminando as características menos importantes.

```python
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE

# Carrega o conjunto de dados Iris
X, y = load_iris(return_X_y=True)

# Inicializa SVC como o estimador externo
estimator = SVC(kernel="linear")

# Inicializa RFE com o estimador externo e seleciona 2 características
selector = RFE(estimator, n_features_to_select=2)

# Seleciona as melhores características
X_selected = selector.fit_transform(X, y)

print("Forma original de X:", X.shape)
print("Forma de X com características selecionadas:", X_selected.shape)
print("Características selecionadas:", selector.get_support(indices=True))
```

Neste exemplo, usamos um Classificador de Vetores de Suporte (SVC) como o estimador externo e selecionamos as duas melhores características do conjunto de dados Iris. A saída mostrará a forma original do conjunto de dados e a forma após a seleção das melhores características.

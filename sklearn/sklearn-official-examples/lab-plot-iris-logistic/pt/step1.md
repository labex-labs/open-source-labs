# Carregar o Conjunto de Dados e Pré-processar

Usaremos a biblioteca scikit-learn para carregar o conjunto de dados Iris. O conjunto de dados contém 3 classes de 50 instâncias cada, onde cada classe se refere a um tipo de planta de íris. Cada instância tem 4 características: comprimento da sépala, largura da sépala, comprimento da pétala e largura da pétala.

```python
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay

# carregar o conjunto de dados Iris
iris = datasets.load_iris()
X = iris.data[:, :2]  # apenas as duas primeiras características são utilizadas.
Y = iris.target
```

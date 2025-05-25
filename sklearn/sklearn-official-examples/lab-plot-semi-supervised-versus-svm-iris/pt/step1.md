# Carregar o conjunto de dados Iris e dividir os dados

Vamos carregar o conjunto de dados Iris, um conjunto de dados amplamente utilizado em aprendizado de máquina para tarefas de classificação. O conjunto de dados contém 150 amostras de flores Iris, com quatro características para cada amostra: comprimento da sépala, largura da sépala, comprimento da pétala e largura da pétala. Vamos dividir o conjunto de dados em características de entrada e rótulos de destino.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# Carregar o conjunto de dados Iris
iris = datasets.load_iris()

# Dividir o conjunto de dados em características de entrada e rótulos de destino
X = iris.data[:, :2] # Usaremos apenas as duas primeiras características para fins de visualização
y = iris.target
```

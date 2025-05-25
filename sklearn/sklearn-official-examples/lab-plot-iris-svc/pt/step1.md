# Importar bibliotecas necessárias e carregar o conjunto de dados

```python
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.inspection import DecisionBoundaryDisplay

# importar alguns dados para trabalhar
iris = datasets.load_iris()
# Tomar as duas primeiras características. Poderíamos evitar isto usando um conjunto de dados bidimensional
X = iris.data[:, :2]
y = iris.target
```

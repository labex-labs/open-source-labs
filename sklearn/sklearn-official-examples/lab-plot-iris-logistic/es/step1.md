# Cargar el conjunto de datos y preprocesar

Usaremos la biblioteca scikit-learn para cargar el conjunto de datos Iris. El conjunto de datos contiene 3 clases de 50 instancias cada una, donde cada clase se refiere a un tipo de planta de iris. Cada instancia tiene 4 características: longitud del sépalo, ancho del sépalo, longitud del pétalo y ancho del pétalo.

```python
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay

# load the Iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
Y = iris.target
```

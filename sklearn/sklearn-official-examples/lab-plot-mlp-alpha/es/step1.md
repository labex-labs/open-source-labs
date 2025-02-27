# Importar bibliotecas

Comenzaremos importando las bibliotecas necesarias para esta práctica. Utilizaremos scikit-learn para crear conjuntos de datos sintéticos, MLPClassifier para construir el modelo MLP, StandardScaler para estandarizar los datos y make_pipeline para crear una tubería de transformaciones y clasificador.

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
```

# Importar Bibliotecas

Começaremos importando as bibliotecas necessárias para este laboratório. Usaremos o scikit-learn para criar conjuntos de dados sintéticos, `MLPClassifier` para construir o modelo MLP, `StandardScaler` para padronizar os dados e `make_pipeline` para criar um pipeline de transformações e classificador.

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

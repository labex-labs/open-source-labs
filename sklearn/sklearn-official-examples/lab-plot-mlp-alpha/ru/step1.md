# Импорт библиотек

Начнем с импорта необходимых библиотек для этого практического занятия. Будем использовать scikit - learn для создания синтетических наборов данных, MLPClassifier для построения модели MLP, StandardScaler для стандартизации данных и make_pipeline для создания конвейера преобразований и классификатора.

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

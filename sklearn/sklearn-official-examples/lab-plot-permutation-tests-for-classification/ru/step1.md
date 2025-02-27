# Загрузка набора данных и генерация случайных признаков

Мы будем использовать набор данных iris, который состоит из измерений трех типов ирисок, и сгенерируем некоторые случайные данные признаков (то есть 20 признаков), не связанные с метками классов в наборе данных iris.

```python
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

n_uncorrelated_features = 20
rng = np.random.RandomState(seed=0)
X_rand = rng.normal(size=(X.shape[0], n_uncorrelated_features))
```

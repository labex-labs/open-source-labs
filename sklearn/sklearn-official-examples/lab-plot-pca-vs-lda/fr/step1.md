# Charger l'ensemble de données

Tout d'abord, nous devons charger l'ensemble de données Iris à l'aide de la fonction `load_iris()` intégrée dans scikit-learn.

```python
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names
```

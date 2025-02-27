# Charger les données

Nous allons charger l'ensemble de données iris à l'aide du module `datasets` de Scikit-Learn. Nous n'utiliserons que deux caractéristiques : la longueur du sépale et la longueur du pétale.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, [0, 2]]
y = iris.target
```

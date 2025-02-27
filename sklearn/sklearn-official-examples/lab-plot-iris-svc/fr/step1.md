# Importez les bibliothèques nécessaires et chargez le jeu de données

```python
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.inspection import DecisionBoundaryDisplay

# importez quelques données pour jouer
iris = datasets.load_iris()
# Prenez les deux premières caractéristiques. Nous pourrions éviter cela en utilisant un jeu de données à deux dimensions
X = iris.data[:, :2]
y = iris.target
```

# Comprendre les ensembles de données

Scikit-learn représente les ensembles de données sous forme de tableaux 2D, où le premier axe représente les échantillons et le second axe représente les caractéristiques. Jetons un coup d'œil à un exemple en utilisant l'ensemble de données iris :

```python
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data
print(data.shape)
```

Sortie :

```
(150, 4)
```

L'ensemble de données iris est composé de 150 observations d'iris, chaque observation étant décrite par 4 caractéristiques. La forme du tableau de données est (150, 4).

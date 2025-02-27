# Construction d'un pipeline avec une réduction de dimensionnalité et un classifieur

Dans cette étape, nous allons construire un pipeline avec une étape de réduction de dimensionnalité et un classifieur, et afficher sa représentation visuelle.

Tout d'abord, nous importons les modules nécessaires :

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA
```

Ensuite, nous définissons les étapes du pipeline :

```python
steps = [("réduire_dim", PCA(n_components=4)), ("classifieur", SVC(kernel="linéaire"))]
```

Ensuite, nous créons le pipeline :

```python
pipe = Pipeline(steps)
```

Enfin, nous affichons la représentation visuelle du pipeline :

```python
pipe
```

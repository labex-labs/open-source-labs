# Construction d'un pipeline enchaînant plusieurs étapes de prétraitement et un classifieur

Dans cette étape, nous allons construire un pipeline avec plusieurs étapes de prétraitement et un classifieur, et afficher sa représentation visuelle.

Tout d'abord, nous importons les modules nécessaires :

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression
```

Ensuite, nous définissons les étapes du pipeline :

```python
steps = [
    ("standard_scaler", StandardScaler()),
    ("polynôme", PolynomialFeatures(degree=3)),
    ("classifieur", LogisticRegression(C=2.0)),
]
```

Ensuite, nous créons le pipeline :

```python
pipe = Pipeline(steps)
```

Enfin, nous affichons la représentation visuelle du pipeline :

```python
pipe
```

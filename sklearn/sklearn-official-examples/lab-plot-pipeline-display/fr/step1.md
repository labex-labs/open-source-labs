# Construction d'un pipeline simple avec une étape de prétraitement et un classifieur

Dans cette étape, nous allons construire un pipeline simple avec une étape de prétraitement et un classifieur, et afficher sa représentation visuelle.

Tout d'abord, nous importons les modules nécessaires :

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import set_config
```

Ensuite, nous définissons les étapes du pipeline :

```python
steps = [
    ("prétraitement", StandardScaler()),
    ("classifieur", LogisticRegression()),
]
```

Ensuite, nous créons le pipeline :

```python
pipe = Pipeline(steps)
```

Enfin, nous affichons la représentation visuelle du pipeline :

```python
set_config(display="diagram")
pipe
```

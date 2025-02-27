# Génération de données

Nous allons générer une tâche de classification à l'aide de la fonction `make_classification` de scikit-learn. Nous allons générer 500 échantillons avec 15 caractéristiques, dont 3 sont informatives, 2 sont redondantes et 10 sont non-informatives.

```python
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=500,
    n_features=15,
    n_informative=3,
    n_redundant=2,
    n_repeated=0,
    n_classes=8,
    n_clusters_per_class=1,
    class_sep=0.8,
    random_state=0,
)
```

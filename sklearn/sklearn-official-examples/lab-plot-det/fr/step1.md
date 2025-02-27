# Générer des données synthétiques

Nous allons utiliser la fonction `make_classification` de scikit-learn pour générer des données synthétiques. Cette fonction génère un problème de classification aléatoire à n classes, avec n_informative caractéristiques informatives, n_redundant caractéristiques redondantes et n_clusters_per_class grappes par classe. Nous allons générer 1000 échantillons avec 2 caractéristiques informatives et un état aléatoire de 1. Nous allons ensuite diviser les données en ensembles d'entraînement et de test avec un ratio de 60/40.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=1_000,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=1,
    n_clusters_per_class=1,
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```

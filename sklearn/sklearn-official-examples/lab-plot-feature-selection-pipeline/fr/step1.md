# Générer et diviser l'ensemble de données

Nous commencerons par générer un ensemble de données de classification binaire à l'aide de la fonction `make_classification` de Scikit-learn. Nous diviserons également l'ensemble de données en sous-ensembles d'entraînement et de test à l'aide de la fonction `train_test_split` de Scikit-learn.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_features=20,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    n_clusters_per_class=2,
    random_state=42,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
```

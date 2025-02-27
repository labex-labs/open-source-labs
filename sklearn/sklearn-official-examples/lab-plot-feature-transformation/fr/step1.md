# Préparation des données

Tout d'abord, nous allons créer un grand ensemble de données de 80 000 échantillons et le diviser en trois ensembles :

- Un ensemble pour entraîner les méthodes d'ensemble qui seront ultérieurement utilisées comme un transformateur d'ingénierie des caractéristiques
- Un ensemble pour entraîner le modèle linéaire
- Un ensemble pour tester le modèle linéaire.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=80_000, random_state=10)

X_full_train, X_test, y_full_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=10
)

X_train_ensemble, X_train_linear, y_train_ensemble, y_train_linear = train_test_split(
    X_full_train, y_full_train, test_size=0.5, random_state=10
)
```

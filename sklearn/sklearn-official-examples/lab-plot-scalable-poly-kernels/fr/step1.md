# Charger et préparer les données

Nous allons tout d'abord charger le jeu de données Covtype et le transformer en un problème de classification binaire en sélectionnant seulement une classe. Ensuite, nous allons diviser les données en un ensemble d'entraînement et un ensemble de test, et normaliser les caractéristiques.

```python
from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, Normalizer

# Charger le jeu de données Covtype, en sélectionnant seulement une classe
X, y = fetch_covtype(return_X_y=True)
y[y!= 2] = 0
y[y == 2] = 1

# Diviser les données en un ensemble d'entraînement et un ensemble de test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=5000, test_size=10000, random_state=42
)

# Normaliser les caractéristiques
mm = make_pipeline(MinMaxScaler(), Normalizer())
X_train = mm.fit_transform(X_train)
X_test = mm.transform(X_test)
```

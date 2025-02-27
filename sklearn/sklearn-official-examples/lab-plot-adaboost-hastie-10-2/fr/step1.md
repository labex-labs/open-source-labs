# Préparer les données et les modèles de base

Nous commençons par générer l'ensemble de données de classification binaire utilisé dans Hastie et al. 2009, Exemple 10.2. Ensuite, nous définissons les hyperparamètres pour nos classifieurs AdaBoost. Nous divisons les données en un ensemble d'entraînement et un ensemble de test. Après cela, nous entraînons nos classifieurs de base, un `DecisionTreeClassifier` avec `depth=9` et un `DecisionTreeClassifier` "d'arbre simple" avec `depth=1` et calculons l'erreur sur le test.

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = datasets.make_hastie_10_2(n_samples=12_000, random_state=1)

n_estimators = 400
learning_rate = 1.0

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=2_000, shuffle=False
)

dt_stump = DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)
dt_stump.fit(X_train, y_train)
dt_stump_err = 1.0 - dt_stump.score(X_test, y_test)

dt = DecisionTreeClassifier(max_depth=9, min_samples_leaf=1)
dt.fit(X_train, y_train)
dt_err = 1.0 - dt.score(X_test, y_test)
```

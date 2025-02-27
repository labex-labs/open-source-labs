# Diviser l'ensemble de données en ensembles d'entraînement et de test

Ensuite, nous allons diviser l'ensemble de données en ensembles d'entraînement et de test en utilisant la fonction `train_test_split` du module `sklearn.model_selection`. L'ensemble d'entraînement sera utilisé pour entraîner le classifieur Naïf Bayésien, et l'ensemble de test sera utilisé pour évaluer ses performances.

```python
from sklearn.model_selection import train_test_split

# Divise l'ensemble de données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

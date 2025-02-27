# Régression multioutput

#### Description du problème

La régression multioutput prédit plusieurs propriétés numériques pour chaque échantillon. Chaque propriété est une variable numérique, et le nombre de propriétés peut être supérieur ou égal à deux.

#### Format de la cible

Une représentation valide des cibles de régression multioutput est une matrice dense, où chaque ligne représente un échantillon et chaque colonne représente une propriété différente.

#### Exemple

Créons un problème de régression multioutput en utilisant la fonction make_regression :

```python
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression

# Générez un problème de régression multioutput
X, y = make_regression(n_samples=100, n_features=10, n_targets=3, random_state=0)

# Ajustez un modèle de régression linéaire multioutput
model = MultiOutputRegressor(LinearRegression())
model.fit(X, y)

# Faites des prédictions
predictions = model.predict(X)
print(predictions)
```

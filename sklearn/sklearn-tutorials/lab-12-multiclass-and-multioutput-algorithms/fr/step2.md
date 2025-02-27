# Classification multilabel

#### Description du problème

La classification multilabel est une tâche de classification où chaque échantillon peut être assigné plusieurs étiquettes. Le nombre d'étiquettes que chaque échantillon peut avoir est supérieur à deux.

#### Format de la cible

Une représentation valide des cibles multilabel est une matrice binaire, où chaque ligne représente un échantillon et chaque colonne représente une classe. Une valeur de 1 indique la présence de l'étiquette dans l'échantillon, tandis que 0 ou -1 indique son absence.

#### Exemple

Créons un problème de classification multilabel en utilisant la fonction make_classification :

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier

# Générez un problème de classification multilabel
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, random_state=0)
y = y.reshape(-1, 1)

# Ajustez un classifieur de forêt aléatoire multioutput
model = MultiOutputClassifier(RandomForestClassifier())
model.fit(X, y)

# Faites des prédictions
predictions = model.predict(X)
print(predictions)
```

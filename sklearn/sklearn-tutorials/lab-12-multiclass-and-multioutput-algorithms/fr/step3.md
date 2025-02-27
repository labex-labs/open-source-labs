# Classification multiclasse-multioutput

#### Description du problème

La classification multiclasse-multioutput, également connue sous le nom de classification multitâche, prédit plusieurs propriétés non binaires pour chaque échantillon. Chaque propriété peut avoir plus de deux classes.

#### Format de la cible

Une représentation valide des cibles multiclasse-multioutput est une matrice dense, où chaque ligne représente un échantillon et chaque colonne représente une propriété ou une classe différente.

#### Exemple

Créons un problème de classification multiclasse-multioutput en utilisant la fonction make_classification :

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC

# Générez un problème de classification multiclasse-multioutput
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_classes=3, random_state=0)

# Ajustez un classifieur à vecteurs de support multioutput
model = MultiOutputClassifier(SVC())
model.fit(X, y)

# Faites des prédictions
predictions = model.predict(X)
print(predictions)
```

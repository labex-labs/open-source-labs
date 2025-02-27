# Classification multiclasse

#### Description du problème

La classification multiclasse est une tâche de classification avec plus de deux classes. Chaque échantillon est assigné à une seule classe.

#### Format de la cible

Une représentation valide des cibles multiclasse est un vecteur 1D ou colonne contenant plus de deux valeurs discrètes.

#### Exemple

Utilisons le jeu de données Iris pour démontrer la classification multiclasse :

```python
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# Chargez le jeu de données Iris
X, y = datasets.load_iris(return_X_y=True)

# Ajustez un modèle de régression logistique en utilisant OneVsRestClassifier
model = OneVsRestClassifier(LogisticRegression())
model.fit(X, y)

# Faites des prédictions
predictions = model.predict(X)
print(predictions)
```

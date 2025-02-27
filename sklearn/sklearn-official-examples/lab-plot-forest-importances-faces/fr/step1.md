# Charger les données et ajuster le modèle

Nous commençons par charger l'ensemble de données Olivetti Faces et en limitant le contenu aux cinq premières classes seulement. Ensuite, nous entraînons une forêt aléatoire sur cet ensemble de données et évaluons l'importance des fonctionnalités basée sur l'impureté. Nous allons définir le nombre de coeurs à utiliser pour les tâches.

```python
from sklearn.datasets import fetch_olivetti_faces

# Nous sélectionnons le nombre de coeurs à utiliser pour effectuer l'ajustement parallèle du
# modèle de forêt. `-1` signifie utiliser tous les coeurs disponibles.
n_jobs = -1

# Charger l'ensemble de données de visages
data = fetch_olivetti_faces()
X, y = data.data, data.target

# Limiter l'ensemble de données aux 5 classes.
mask = y < 5
X = X[mask]
y = y[mask]

# Un classifieur de forêt aléatoire sera ajusté pour calculer l'importance des fonctionnalités.
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators=750, n_jobs=n_jobs, random_state=42)

forest.fit(X, y)
```

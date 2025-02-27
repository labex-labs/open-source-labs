# Importation des bibliothèques et chargement de l'ensemble de données

Commenceons par importer les bibliothèques nécessaires et charger l'ensemble de données iris. Nous utiliserons la fonction `load_iris` du module `sklearn.datasets` pour charger l'ensemble de données.

```python
from sklearn.datasets import load_iris

# Charge l'ensemble de données iris
iris = load_iris()
X = iris.data  # Caractéristiques
y = iris.target  # Variable cible

print("Nombre d'échantillons :", X.shape[0])
print("Nombre de caractéristiques :", X.shape[1])
print("Nombre de classes :", len(set(y)))
```

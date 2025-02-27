# Importation des bibliothèques et génération du jeu de données

Nous commençons par importer les bibliothèques nécessaires et en générant un jeu de données de classification binaire synthétique avec 100 000 échantillons et 20 caractéristiques. Parmi les 20 caractéristiques, seulement 2 sont informatives, 2 sont redondantes et les 16 restantes sont non informatives. Parmi les 100 000 échantillons, 100 seront utilisés pour l'ajustement du modèle et le reste pour les tests.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Générer le jeu de données
X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=2, random_state=42
)

train_samples = 100  # Échantillons utilisés pour entraîner les modèles
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    shuffle=False,
    test_size=100_000 - train_samples,
)
```

# Ensemble de données

Nous utiliserons un ensemble de données de classification binaire synthétique avec 100 000 échantillons et 20 caractéristiques. Parmi les 20 caractéristiques, seulement 2 sont informatives, 10 sont redondantes (combinaisons aléatoires des caractéristiques informatives) et les 8 restantes sont non informatives (nombres aléatoires). Sur les 100 000 échantillons, 1 000 seront utilisés pour l'ajustement du modèle et le reste pour les tests.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=10, random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.99, random_state=42
)
```

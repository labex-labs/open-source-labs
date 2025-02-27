# Charger et préparer les données

Nous allons charger l'ensemble de données sur le vin à partir de scikit-learn et le diviser en ensembles d'entraînement et de test. Nous allons également mettre à l'échelle les fonctionnalités dans l'ensemble d'entraînement en utilisant le StandardScaler du module de prétraitement scikit-learn.

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = load_wine(return_X_y=True, as_frame=True)
scaler = StandardScaler().set_output(transform="pandas")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)
scaled_X_train = scaler.fit_transform(X_train)
```

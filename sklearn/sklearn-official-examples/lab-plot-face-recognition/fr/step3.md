# Prétraitement des données

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

Nous divisons l'ensemble de données en un ensemble d'entraînement et un ensemble de test et prétraitons les données en mettant à l'échelle les données d'entrée à l'aide de la fonction `StandardScaler()`.

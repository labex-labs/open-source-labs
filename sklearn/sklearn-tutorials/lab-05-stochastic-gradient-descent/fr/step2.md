# Chargez et prétraitez les données

Ensuite, nous allons charger l'ensemble de données iris et le prétraiter en mettant à l'échelle les caractéristiques à l'aide de StandardScaler.

```python
# Chargez l'ensemble de données iris
iris = load_iris()
X, y = iris.data, iris.target

# Mettez à l'échelle les caractéristiques
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Divisez les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```

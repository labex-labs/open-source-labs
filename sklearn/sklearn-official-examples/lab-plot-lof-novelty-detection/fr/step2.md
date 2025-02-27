# Générer des données

Nous allons générer des données pour l'entraînement, les tests et les anomalies à l'aide de numpy. Nous allons générer 100 observations d'entraînement normales, 20 observations de test normales et 20 observations de nouveauté anormales.

```python
np.random.seed(42)

xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```

# Générer des données avec des anomalies

Nous allons générer un ensemble de données composé de 120 points de données, avec 100 données normales et 20 anomalies. Nous allons ensuite tracer les données pour visualiser les anomalies.

```python
np.random.seed(42)

X_inliers = 0.3 * np.random.randn(100, 2)
X_inliers = np.r_[X_inliers + 2, X_inliers - 2]
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
X = np.r_[X_inliers, X_outliers]

plt.scatter(X[:, 0], X[:, 1], color="k", s=3.0)
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.xlabel("Data points")
plt.title("Data with Outliers")
plt.show()
```

# Generar datos con valores atípicos

Generaremos un conjunto de datos de 120 puntos de datos con 100 valores normales y 20 valores atípicos. Luego graficaremos los datos para visualizar los valores atípicos.

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

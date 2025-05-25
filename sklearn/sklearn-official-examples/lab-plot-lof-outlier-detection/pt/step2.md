# Gerar Dados com Outliers

Vamos gerar um conjunto de dados com 120 pontos de dados, 100 inliers e 20 outliers. Em seguida, vamos representar graficamente os dados para visualizar os outliers.

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
plt.xlabel("Pontos de dados")
plt.title("Dados com Outliers")
plt.show()
```

# Daten mit Ausreißern generieren

Wir werden einen Datensatz von 120 Datenpunkten mit 100 Innerpunkten und 20 Ausreißern generieren. Anschließend werden wir die Daten plotten, um die Ausreißer zu visualisieren.

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

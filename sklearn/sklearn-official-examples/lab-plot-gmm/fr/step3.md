# Implémenter le modèle de mélange gaussien

Dans cette étape, nous allons implémenter le modèle de mélange gaussien à l'aide de la classe `GaussianMixture` de scikit-learn. Nous allons ajuster le modèle à notre ensemble de données et prédire les étiquettes de cluster pour chaque point de données. Enfin, nous allons tracer les résultats.

```python
# Create a GMM object with 5 components
gmm = mixture.GaussianMixture(n_components=5, covariance_type="full")

# Fit the GMM to the data
gmm.fit(X)

# Predict the cluster labels
Y_ = gmm.predict(X)

# Plot the results
color_iter = ["navy", "c", "cornflowerblue", "gold", "darkorange"]

for i, color in enumerate(color_iter):
    plt.scatter(
        X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color, label="Cluster {}".format(i)
    )

plt.legend(loc="best")
plt.title("Gaussian Mixture Model")
plt.show()
```

# Implémenter le modèle de mélange gaussien bayésien

Dans cette étape, nous allons implémenter le modèle de mélange gaussien bayésien à l'aide de la classe `BayesianGaussianMixture` de scikit-learn. Ce modèle a une loi a priori de processus de Dirichlet qui adapte automatiquement le nombre de clusters en fonction des données. Nous allons ajuster le modèle à notre ensemble de données et prédire les étiquettes de cluster pour chaque point de données. Enfin, nous allons tracer les résultats.

```python
# Create a Bayesian GMM object with 5 components
dpgmm = mixture.BayesianGaussianMixture(n_components=5, covariance_type="full")

# Fit the Bayesian GMM to the data
dpgmm.fit(X)

# Predict the cluster labels
Y_ = dpgmm.predict(X)

# Plot the results
color_iter = ["navy", "c", "cornflowerblue", "gold", "darkorange"]

for i, color in enumerate(color_iter):
    plt.scatter(
        X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color, label="Cluster {}".format(i)
    )

plt.legend(loc="best")
plt.title("Bayesian Gaussian Mixture Model with a Dirichlet process prior")
plt.show()
```

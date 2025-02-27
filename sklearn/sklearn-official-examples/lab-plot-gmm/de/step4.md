# Bayesisches Gauß'sches Mischmodell implementieren

In diesem Schritt implementieren wir das Bayes'sche Gauß'sche Mischmodell mithilfe der `BayesianGaussianMixture`-Klasse von scikit-learn. Dieses Modell hat einen Dirichlet-Prozess-Prior, der automatisch die Anzahl der Cluster basierend auf den Daten anpasst. Wir werden das Modell an unseren Datensatz anpassen und die Clusterbezeichnungen für jedes Datenpunkt vorherhersagen. Schließlich werden wir die Ergebnisse darstellen.

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
plt.title("Bayesisches Gauß'sches Mischmodell mit Dirichlet-Prozess-Prior")
plt.show()
```

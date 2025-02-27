# Gauß'sches Mischmodell implementieren

In diesem Schritt implementieren wir das Gauß'sche Mischmodell mithilfe der `GaussianMixture`-Klasse von scikit-learn. Wir werden das Modell an unseren Datensatz anpassen und die Clusterbezeichnungen für jedes Datenpunkt vorherhersagen. Schließlich werden wir die Ergebnisse darstellen.

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
plt.title("Gauß'sches Mischmodell")
plt.show()
```

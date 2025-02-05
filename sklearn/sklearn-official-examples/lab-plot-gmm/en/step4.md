# Implement Bayesian Gaussian Mixture Model

In this step, we will implement the Bayesian Gaussian Mixture Model using the `BayesianGaussianMixture` class of scikit-learn. This model has a Dirichlet process prior that automatically adapts the number of clusters based on the data. We will fit the model to our dataset and predict the cluster labels for each data point. Finally, we will plot the results.

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

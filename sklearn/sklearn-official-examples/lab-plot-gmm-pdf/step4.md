# Plot Density Estimation

We will now plot the density estimation of the mixture of Gaussians. We will create a meshgrid of points over the range of the dataset and calculate the negative log-likelihood predicted by the GMM for each point. We will then display the predicted scores as a contour plot and scatter plot the training data.

```python
# display predicted scores by the model as a contour plot
x = np.linspace(-20.0, 30.0)
y = np.linspace(-20.0, 40.0)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -clf.score_samples(XX)
Z = Z.reshape(X.shape)

CS = plt.contour(
    X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0), levels=np.logspace(0, 3, 10)
)
CB = plt.colorbar(CS, shrink=0.8, extend="both")
plt.scatter(X_train[:, 0], X_train[:, 1], 0.8)

plt.title("Density Estimation with Gaussian Mixture Models")
plt.axis("tight")
plt.show()
```

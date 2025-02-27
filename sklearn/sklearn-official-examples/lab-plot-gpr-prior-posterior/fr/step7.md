# Noyau de produit scalaire

Le noyau de produit scalaire est défini comme suit :

$$
k(x_i, x_j) = (\sigma_0 + x_i^T x_j)^2
$$

où $\sigma_0$ est une constante.

```python
kernel = ConstantKernel(0.1, (0.01, 10.0)) * (
    DotProduct(sigma_0=1.0, sigma_0_bounds=(0.1, 10.0)) ** 2
)
gpr = GaussianProcessRegressor(kernel=kernel, random_state=0)

fig, axs = plt.subplots(nrows=2, sharex=True, sharey=True, figsize=(10, 8))

# trace la distribution a priori
plot_gpr_samples(gpr, n_samples=n_samples, ax=axs[0])
axs[0].set_title("Echantillons de la distribution a priori")

# trace la distribution a posteriori
gpr.fit(X_train, y_train)
plot_gpr_samples(gpr, n_samples=n_samples, ax=axs[1])
axs[1].scatter(X_train[:, 0], y_train, color="red", zorder=10, label="Observations")
axs[1].legend(bbox_to_anchor=(1.05, 1.5), loc="upper left")
axs[1].set_title("Echantillons de la distribution a posteriori")

fig.suptitle("Noyau de produit scalaire", fontsize=18)
plt.tight_layout()
```

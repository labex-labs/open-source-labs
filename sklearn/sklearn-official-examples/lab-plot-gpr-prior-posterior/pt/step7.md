# Kernel Produto Escalar

O kernel Produto Escalar é definido como:

$$
k(x_i, x_j) = (\sigma_0 + x_i^T x_j)^2
$$

onde $\sigma_0$ é uma constante.

```python
kernel = ConstantKernel(0.1, (0.01, 10.0)) * (
    DotProduct(sigma_0=1.0, sigma_0_bounds=(0.1, 10.0)) ** 2
)
gpr = GaussianProcessRegressor(kernel=kernel, random_state=0)

fig, axs = plt.subplots(nrows=2, sharex=True, sharey=True, figsize=(10, 8))

# plotar a priori
plot_gpr_samples(gpr, n_samples=n_samples, ax=axs[0])
axs[0].set_title("Amostras da distribuição a priori")

# plotar a posteriori
gpr.fit(X_train, y_train)
plot_gpr_samples(gpr, n_samples=n_samples, ax=axs[1])
axs[1].scatter(X_train[:, 0], y_train, color="red", zorder=10, label="Observações")
axs[1].legend(bbox_to_anchor=(1.05, 1.5), loc="upper left")
axs[1].set_title("Amostras da distribuição a posteriori")

fig.suptitle("Kernel Produto Escalar", fontsize=18)
plt.tight_layout()
```

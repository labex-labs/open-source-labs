# Kernel Racional Quadrático

O kernel Racional Quadrático é definido como:

$$
k(x_i, x_j) = \left( 1 + \frac{\|x_i - x_j\|^2}{2\alpha\ell^2} \right)^{-\alpha}
$$

onde $\ell$ é o parâmetro de escala de comprimento e $\alpha$ controla o peso relativo de características de pequena e grande escala.

```python
kernel = 1.0 * RationalQuadratic(length_scale=1.0, alpha=0.1, alpha_bounds=(1e-5, 1e15))
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

fig.suptitle("Kernel Racional Quadrático", fontsize=18)
plt.tight_layout()
```

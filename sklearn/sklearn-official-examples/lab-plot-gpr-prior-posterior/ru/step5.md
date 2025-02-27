# Ядро с рациональным квадратичным ядром

Ядро с рациональным квадратичным ядром определяется как:

$$
k(x_i, x_j) = \left( 1 + \frac{\|x_i - x_j\|^2}{2\alpha\ell^2} \right)^{-\alpha}
$$

где $\ell$ - параметр длины масштаба, а $\alpha$ контролирует относительный вес мелких и крупных масштабных признаков.

```python
kernel = 1.0 * RationalQuadratic(length_scale=1.0, alpha=0.1, alpha_bounds=(1e-5, 1e15))
gpr = GaussianProcessRegressor(kernel=kernel, random_state=0)

fig, axs = plt.subplots(nrows=2, sharex=True, sharey=True, figsize=(10, 8))

# plot prior
plot_gpr_samples(gpr, n_samples=n_samples, ax=axs[0])
axs[0].set_title("Samples from prior distribution")

# plot posterior
gpr.fit(X_train, y_train)
plot_gpr_samples(gpr, n_samples=n_samples, ax=axs[1])
axs[1].scatter(X_train[:, 0], y_train, color="red", zorder=10, label="Observations")
axs[1].legend(bbox_to_anchor=(1.05, 1.5), loc="upper left")
axs[1].set_title("Samples from posterior distribution")

fig.suptitle("Rational Quadratic kernel", fontsize=18)
plt.tight_layout()
```

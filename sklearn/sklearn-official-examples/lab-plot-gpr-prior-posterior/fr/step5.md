# Noyau quadratique rationnel

Le noyau quadratique rationnel est défini comme suit :

$$
k(x_i, x_j) = \left( 1 + \frac{\|x_i - x_j\|^2}{2\alpha\ell^2} \right)^{-\alpha}
$$

où $\ell$ est le paramètre d'échelle de longueur et $\alpha$ contrôle le poids relatif des caractéristiques à petite et à grande échelle.

```python
kernel = 1.0 * RationalQuadratic(length_scale=1.0, alpha=0.1, alpha_bounds=(1e-5, 1e15))
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

fig.suptitle("Noyau quadratique rationnel", fontsize=18)
plt.tight_layout()
```

# Noyau Exp-Sine-Squared

Le noyau Exp-Sine-Squared est défini comme suit :

$$
k(x_i, x_j) = \exp \left( -\frac{2\sin^2(\pi\|x_i - x_j\|/p)}{\ell^2} \right)
$$

où $\ell$ est le paramètre d'échelle de longueur et $p$ contrôle la périodicité.

```python
kernel = 1.0 * ExpSineSquared(
    length_scale=1.0,
    periodicity=3.0,
    length_scale_bounds=(0.1, 10.0),
    periodicity_bounds=(1.0, 10.0),
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

fig.suptitle("Noyau Exp-Sine-Squared", fontsize=18)
plt.tight_layout()
```

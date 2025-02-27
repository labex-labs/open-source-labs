# Noyau de fonction de base radiale

Le noyau de fonction de base radiale (RBF) est défini comme suit :

$$
k(x_i, x_j) = \exp \left( -\frac{\|x_i - x_j\|^2}{2\ell^2} \right)
$$

où $\ell$ est le paramètre d'échelle de longueur.

```python
kernel = 1.0 * RBF(length_scale=1.0, length_scale_bounds=(1e-1, 10.0))
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

fig.suptitle("Noyau de fonction de base radiale", fontsize=18)
plt.tight_layout()
```

# Créez un graphique avec une échelle logit et une notation de survie

Nous allons créer un graphique avec une échelle logit et une notation de survie. Cela peut être fait en définissant l'échelle de l'axe y sur logit et en définissant le paramètre `one_half` sur `"1/2"` et le paramètre `use_overline` sur `True` en utilisant `set_yscale("logit", one_half="1/2", use_overline=True)`. Nous allons également tracer les fonctions de distribution cumulative pour les distributions normale, laplacienne et de Cauchy en utilisant `plot()` et ajouter une légende en utilisant `legend()`.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.set_yscale("logit", one_half="1/2", use_overline=True)
axs.set_ylim(1e-5, 1 - 1e-5)
axs.legend()
axs.grid()

plt.show()
```

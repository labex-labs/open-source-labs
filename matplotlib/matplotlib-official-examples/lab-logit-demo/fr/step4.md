# Créez un graphique avec une échelle linéaire

Nous allons créer un graphique avec une échelle linéaire. Cela peut être fait en traçant simplement les fonctions de distribution cumulative pour les distributions normale, laplacienne et de Cauchy en utilisant `plot()` et en ajoutant une légende en utilisant `legend()`.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.legend()
axs.grid()

plt.show()
```

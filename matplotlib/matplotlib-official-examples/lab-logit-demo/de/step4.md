# Erstellen eines Plots mit linearer Skala

Wir werden einen Plot mit linearer Skala erstellen. Dies kann einfach dadurch erreicht werden, dass man die kumulativen Verteilungsfunktionen für die Normal-, Laplace- und Cauchy-Verteilungen mit `plot()` plotten und eine Legende mit `legend()` hinzufügen.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.legend()
axs.grid()

plt.show()
```

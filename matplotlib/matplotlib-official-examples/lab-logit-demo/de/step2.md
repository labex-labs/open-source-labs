# Erstellen eines Plots mit Logit-Skala und Standardnotation

Wir werden einen Plot mit Logit-Skala und Standardnotation erstellen. Dies kann erreicht werden, indem die y-Achsen-Skala auf Logit gesetzt wird, indem man `set_yscale("logit")` verwendet, und die y-Achsen-Grenzen mit `set_ylim()` festlegt. Wir werden auch die kumulativen Verteilungsfunktionen für die Normal-, Laplace- und Cauchy-Verteilungen mit `plot()` plotten und eine Legende mit `legend()` hinzufügen.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.set_yscale("logit")
axs.set_ylim(1e-5, 1 - 1e-5)
axs.legend()
axs.grid()

plt.show()
```

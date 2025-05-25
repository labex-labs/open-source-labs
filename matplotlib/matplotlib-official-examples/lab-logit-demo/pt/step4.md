# Criar um gráfico com escala linear

Criaremos um gráfico com escala linear. Isso pode ser feito simplesmente plotando as funções de distribuição cumulativa para as distribuições normal, Laplaciana e Cauchy usando `plot()` e adicionando uma legenda usando `legend()`.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.legend()
axs.grid()

plt.show()
```

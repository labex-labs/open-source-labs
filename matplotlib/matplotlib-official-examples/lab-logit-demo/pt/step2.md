# Criar um gráfico com escala logit e notação padrão

Criaremos um gráfico com escala logit e notação padrão. Isso pode ser feito definindo a escala do eixo y para logit usando `set_yscale("logit")` e definindo os limites do eixo y usando `set_ylim()`. Também plotaremos as funções de distribuição cumulativa para as distribuições normal, Laplaciana e Cauchy usando `plot()` e adicionaremos uma legenda usando `legend()`.

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

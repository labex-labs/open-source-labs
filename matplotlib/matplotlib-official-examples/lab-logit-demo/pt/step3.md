# Criar um gráfico com escala logit e notação de sobrevivência

Criaremos um gráfico com escala logit e notação de sobrevivência. Isso pode ser feito definindo a escala do eixo y para logit e definindo o parâmetro `one_half` para `"1/2"` e o parâmetro `use_overline` para `True` usando `set_yscale("logit", one_half="1/2", use_overline=True)"`. Também plotaremos as funções de distribuição cumulativa para as distribuições normal, Laplaciana e Cauchy usando `plot()` e adicionaremos uma legenda usando `legend()`.

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

# Criar o gráfico

Nesta etapa, criamos o gráfico chamando a função `plot_beta_hist()` e passando os parâmetros.

```python
fig, ax = plt.subplots()
plot_beta_hist(ax, 10, 10)
plot_beta_hist(ax, 4, 12)
plot_beta_hist(ax, 50, 12)
plot_beta_hist(ax, 6, 55)
ax.set_title("'bmh' style sheet")

plt.show()
```

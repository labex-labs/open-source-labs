# Plotar o Conjunto de Dados

Agora, plotamos o conjunto de dados multirótulo gerado aleatoriamente usando a função `plot_2d`. Criamos uma figura com dois subplots e chamamos a função `plot_2d` para cada subplot com diferentes valores de parâmetro.

```python
_, (ax1, ax2) = plt.subplots(1, 2, sharex="row", sharey="row", figsize=(8, 4))
plt.subplots_adjust(bottom=0.15)

p_c, p_w_c = plot_2d(ax1, n_labels=1)
ax1.set_title("n_labels=1, length=50")
ax1.set_ylabel("Contagem da Característica 1")

plot_2d(ax2, n_labels=3)
ax2.set_title("n_labels=3, length=50")
ax2.set_xlim(left=0, auto=True)
ax2.set_ylim(bottom=0, auto=True)

plt.show()
```

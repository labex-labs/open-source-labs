# Criar o Gráfico

Em seguida, criaremos o gráfico usando a função `subplots()` do Matplotlib e plotaremos o preço de fechamento ajustado das ações do Google ao longo do tempo.

```python
fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close)
```

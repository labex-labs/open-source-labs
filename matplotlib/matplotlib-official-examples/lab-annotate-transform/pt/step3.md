# Criar o Gráfico

Agora, criaremos o gráfico usando a biblioteca `matplotlib.pyplot`. Definiremos os limites x e y do gráfico e, em seguida, plotaremos os dados.

```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
```

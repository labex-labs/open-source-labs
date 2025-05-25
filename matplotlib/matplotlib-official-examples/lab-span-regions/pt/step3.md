# Criar o Gráfico

Agora criaremos o gráfico usando `matplotlib.pyplot`. Plotaremos a onda senoidal e adicionaremos uma linha horizontal em y=0.

```python
fig, ax = plt.subplots()

ax.plot(t, s, color='black')
ax.axhline(0, color='black')
```

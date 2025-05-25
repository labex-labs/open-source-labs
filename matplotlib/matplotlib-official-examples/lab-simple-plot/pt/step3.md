# Criar o gráfico

Agora que temos os dados, podemos criar o gráfico. Primeiro, criamos um objeto de figura e eixo usando `plt.subplots()`. Em seguida, plotamos os dados usando `ax.plot()`.

```python
fig, ax = plt.subplots()
ax.plot(t, s)
```

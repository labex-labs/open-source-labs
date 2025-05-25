# Criar um gráfico e definir o eixo x para escala logarítmica

Criamos um objeto de figura e eixos usando o método `subplots()`. Em seguida, plotamos a função de decaimento exponencial usando o método `semilogx()` e definimos o eixo x para uma escala logarítmica usando o método `set_xscale()`. Também adicionamos uma grade ao gráfico usando o método `grid()`.

```python
fig, ax = plt.subplots()

ax.semilogx(t, np.exp(-t / 5.0))
ax.set_xscale('log')
ax.grid()
```

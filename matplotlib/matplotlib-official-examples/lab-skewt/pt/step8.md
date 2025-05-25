# Criar o Diagrama SkewT-logP

Agora criaremos o diagrama SkewT-logP usando a projeção SkewXAxes que registramos anteriormente. Primeiro, criaremos um objeto figura e adicionaremos um subplot com a projeção SkewXAxes. Em seguida, plotaremos os dados de temperatura e ponto de orvalho no diagrama usando a função semilogy. Finalmente, definiremos os limites e as marcações (ticks) para os eixos X e Y e exibiremos o gráfico.

```python
fig = plt.figure(figsize=(6.5875, 6.2125))
ax = fig.add_subplot(projection='skewx')

ax.semilogy(T, p, color='C3')
ax.semilogy(Td, p, color='C2')

ax.axvline(0, color='C0')

ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_yticks(np.linspace(100, 1000, 10))
ax.set_ylim(1050, 100)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.set_xlim(-50, 50)

plt.grid(True)
plt.show()
```

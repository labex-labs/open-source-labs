# Criar Gráfico Symlog no eixo x

No primeiro subplot, criaremos um gráfico `symlog` no eixo x. Também adicionaremos uma grade menor ao eixo x.

```python
ax0.plot(x, y1)
ax0.set_xscale('symlog')
ax0.set_ylabel('symlogx')
ax0.grid()
ax0.xaxis.grid(which='minor')
```

# Criar um Gráfico Log-Log com Datalim Ajustável

Em seguida, criaremos um gráfico log-log com um datalim ajustável. Isso significa que tanto o eixo x quanto o eixo y terão escalas logarítmicas, e a proporção do gráfico será ajustada para se adequar aos dados.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_adjustable("datalim")
ax.plot([1, 3, 10], [1, 9, 100], "o-")
ax.set_xlim(1e-1, 1e2)
ax.set_ylim(1e-1, 1e3)
ax.set_aspect(1)
ax.set_title("Gráfico Log-Log com Datalim Ajustável")
plt.show()
```

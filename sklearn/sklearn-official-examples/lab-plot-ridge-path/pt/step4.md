# Visualizar Resultados

Neste passo, visualizaremos os resultados dos caminhos da Regressão Ridge.

```python
ax = plt.gca()

ax.plot(alphas, coefs)
ax.set_xscale("log")
ax.set_xlim(ax.get_xlim()[::-1])  # inverter eixo
plt.xlabel("alpha")
plt.ylabel("pesos")
plt.title("Coeficientes Ridge em função da regularização")
plt.axis("tight")
plt.show()
```

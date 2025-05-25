# Visualizar Dados

Podemos visualizar o conjunto de dados de círculos concêntricos usando um gráfico de dispersão.

```python
ax = plt.subplot(1, 1, 1)
ax.scatter(X[red, 0], X[red, 1], c="r")
ax.scatter(X[green, 0], X[green, 1], c="g")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```

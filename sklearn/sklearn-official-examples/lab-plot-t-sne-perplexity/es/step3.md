# Visualizar datos

Podemos visualizar el conjunto de datos de círculos concéntricos utilizando un diagrama de dispersión.

```python
ax = plt.subplot(1, 1, 1)
ax.scatter(X[red, 0], X[red, 1], c="r")
ax.scatter(X[green, 0], X[green, 1], c="g")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```

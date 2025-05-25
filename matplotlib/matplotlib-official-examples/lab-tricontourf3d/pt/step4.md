# Criar o Gráfico

Agora, criaremos o gráfico usando a função `tricontourf()` e personalizaremos o ângulo de visualização.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontourf(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)

plt.show()
```

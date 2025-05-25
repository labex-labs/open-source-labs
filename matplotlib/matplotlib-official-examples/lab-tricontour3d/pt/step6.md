# Criar gráfico de contorno 3D

Criaremos um gráfico de contorno 3D usando a triangulação criada e as coordenadas z. Também personalizaremos o ângulo de visualização para que seja mais fácil entender o gráfico.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontour(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)
plt.show()
```

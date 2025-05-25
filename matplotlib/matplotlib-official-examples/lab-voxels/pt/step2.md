# Preparar as coordenadas

Em seguida, prepararemos as coordenadas para o nosso gráfico de voxels. Criaremos uma grade de pontos 8x8x8 usando a função `indices` do NumPy.

```python
x, y, z = np.indices((8, 8, 8))
```

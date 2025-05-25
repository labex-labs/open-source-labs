# Criar o gráfico de hastes 3D

Nesta etapa, criaremos o gráfico de hastes 3D usando a função `stem` do Matplotlib. Passaremos as coordenadas x, y e z como argumentos para a função `stem`.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

plt.show()
```

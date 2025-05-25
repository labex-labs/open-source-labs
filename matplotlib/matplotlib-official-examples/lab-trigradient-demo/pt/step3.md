# Criar a Triangulação

```python
triang = Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

Explicação:

- `Triangulation` é uma classe que cria uma triangulação de Delaunay a partir de um conjunto de pontos.
- `triang` é uma instância da classe `Triangulation`.
- `triang.set_mask` mascara os triângulos indesejados.

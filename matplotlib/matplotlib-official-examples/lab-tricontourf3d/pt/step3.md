# Criar uma Triangulação Personalizada

Nesta etapa, criaremos uma triangulação personalizada e mascararemos os triângulos indesejados.

```python
triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

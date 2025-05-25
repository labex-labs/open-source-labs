# Criar a Triangulação

Criaremos a triangulação usando `matplotlib.tri.Triangulation`. Não precisamos especificar os triângulos, então a triangulação de Delaunay dos pontos será criada automaticamente.

```python
triang = tri.Triangulation(x, y)
```

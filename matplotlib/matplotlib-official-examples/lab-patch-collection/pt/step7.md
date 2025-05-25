# Criar polígonos

Criamos polígonos usando `Polygon()` e os adicionamos à lista de patches.

```python
for i in range(N):
    polygon = Polygon(np.random.rand(N, 2), closed=True)
    patches.append(polygon)
```

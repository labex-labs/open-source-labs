# Mascar Triângulos Indesejados

Vamos mascarar os triângulos indesejados calculando a média das coordenadas x e y dos vértices de cada triângulo e comparando-a com o raio mínimo.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

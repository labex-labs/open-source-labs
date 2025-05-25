# Mascar Triângulos Indesejados

Mascaramos os triângulos indesejados calculando o ponto médio de cada triângulo e verificando se ele se enquadra em um raio dado.

```python
xmid = x[triang.triangles].mean(axis=1)
ymid = y[triang.triangles].mean(axis=1)
mask = xmid**2 + ymid**2 < min_radius**2
triang.set_mask(mask)
```

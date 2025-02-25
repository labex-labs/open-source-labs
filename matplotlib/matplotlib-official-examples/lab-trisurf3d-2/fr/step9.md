# Masquer les triangles indésirables

Nous masquons les triangles indésirables en calculant le point milieu de chaque triangle et en vérifiant si celui-ci se trouve à l'intérieur d'un rayon donné.

```python
xmid = x[triang.triangles].mean(axis=1)
ymid = y[triang.triangles].mean(axis=1)
mask = xmid**2 + ymid**2 < min_radius**2
triang.set_mask(mask)
```

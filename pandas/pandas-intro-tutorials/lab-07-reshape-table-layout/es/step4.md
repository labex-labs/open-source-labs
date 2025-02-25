# Crear una tabla dinámica

Crea una tabla dinámica para encontrar las concentraciones promedio de 𝑁𝑂2 y 𝑃𝑀25 en cada una de las estaciones.

```python
air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
```

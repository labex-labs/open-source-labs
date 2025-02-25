# Créer un tableau pivot

Créez un tableau pivot pour trouver les concentrations moyennes de NO2 et PM25 dans chaque station.

```python
air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
```

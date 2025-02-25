# Convertir de formato de tabla larga a ancha

Ahora convertiremos los datos de calidad del aire en formato largo a formato ancho utilizando la función `pivot`.

```python
# Filtrar solo datos de no2
no2 = air_quality[air_quality["parameter"] == "no2"]

# Usar 2 mediciones (head) para cada ubicación (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)

# Hacer pivote de los datos
no2_subset.pivot(columns="location", values="value")
```

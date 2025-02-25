# Crear una nueva columna

Crearemos una nueva columna, "london_mg_per_cubic", multiplicando la columna "station_london" por un factor de conversión.

```python
# Crear una nueva columna multiplicando "station_london" por el factor de conversión
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
```

# Comprobar la relación de valores en dos columnas

A continuación, comprobaremos la relación de los valores en las columnas "station_paris" y "station_antwerp" y guardaremos el resultado en una nueva columna.

```python
# Crear una nueva columna dividiendo "station_paris" entre "station_antwerp"
air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]
```

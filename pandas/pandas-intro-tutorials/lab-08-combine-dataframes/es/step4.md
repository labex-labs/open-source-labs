# Combinar tablas utilizando un identificador común

Luego, agregaremos las coordenadas de las estaciones a la tabla de mediciones utilizando la función `merge`. Realizaremos un join izquierdo en la columna `location`.

```python
# Load the stations coordinates data
stations_coord = pd.read_csv("data/air_quality_stations.csv")

# Merge the air_quality and stations_coord dataframes
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
```

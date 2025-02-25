# Cambiar los nombres de las etiquetas de las columnas

Cambiaremos los nombres de las etiquetas de las columnas para que coincidan con los identificadores de las estaciones utilizados por OpenAQ.

```python
# Cambiar los nombres de las etiquetas de las columnas
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
```

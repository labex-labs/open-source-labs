# Agregar la descripción y nombre completos de los parámetros

Por último, agregaremos la descripción y nombre completos de los parámetros a la tabla de mediciones. Realizamos un join izquierdo en las columnas `parameter` e `id`.

```python
# Load the air quality parameters data
air_quality_parameters = pd.read_csv("data/air_quality_parameters.csv")

# Merge the air_quality and air_quality_parameters dataframes
air_quality = pd.merge(air_quality, air_quality_parameters, how='left', left_on='parameter', right_on='id')
```

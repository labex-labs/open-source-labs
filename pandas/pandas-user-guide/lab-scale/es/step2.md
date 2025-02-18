# Cargar Menos Datos

En lugar de cargar todos los datos, podemos cargar solo las columnas que necesitamos. Aquí, demostramos dos métodos para cargar menos datos del archivo parquet.

```python
# Opción 1: Cargar todos los datos y luego filtrar
columns = ["id_0", "name_0", "x_0", "y_0"]
pd.read_parquet("timeseries_wide.parquet")[columns]

# Opción 2: Cargar solo las columnas solicitadas
pd.read_parquet("timeseries_wide.parquet", columns=columns)
```

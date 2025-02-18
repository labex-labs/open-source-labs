# Utilizar Tipos de Datos Eficientes

Los tipos de datos predeterminados de pandas no son los más eficientes en términos de memoria. Este paso muestra cómo utilizar tipos de datos más eficientes para almacenar conjuntos de datos más grandes en memoria.

```python
ts = make_timeseries(freq="30S", seed=0)
ts.to_parquet("timeseries.parquet")
ts = pd.read_parquet("timeseries.parquet")

# Convertir la columna 'name' al tipo 'category' para mayor eficiencia
ts2 = ts.copy()
ts2["name"] = ts2["name"].astype("category")

# Reducir el tamaño de las columnas numéricas a sus tipos más pequeños
ts2["id"] = pd.to_numeric(ts2["id"], downcast="unsigned")
ts2[["x", "y"]] = ts2[["x", "y"]].apply(pd.to_numeric, downcast="float")
```

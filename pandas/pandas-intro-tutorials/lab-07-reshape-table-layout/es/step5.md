# Convertir de formato ancho a largo

Ahora, convertiremos los datos de 𝑁𝑂2 en formato ancho a formato largo utilizando la función `melt`.

```python
# Restablecer el índice para no2_pivoted
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

# Fundir los datos
no_2 = no2_pivoted.melt(id_vars="date.utc")
```

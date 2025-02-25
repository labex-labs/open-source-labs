# Remuestreo de datos de series de tiempo

El método `resample` es una forma poderosa de cambiar la frecuencia de los datos de series de tiempo. Aquí, agregaremos los datos actuales de series de tiempo horarias al valor máximo mensual en cada estación de medición.

```python
# By pivoting the data, the datetime information became the index of the table.
no_2 = air_quality.pivot(index="datetime", columns="location", values="value")
no_2.head()

# Create a plot of the values in the different stations from the 20th of May till the end of 21st of May
no_2["2019-05-20":"2019-05-21"].plot()

# resample time series data
monthly_max = no_2.resample("M").max()
monthly_max
```

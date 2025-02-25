# Calcular la concentración promedio de NO2 para cada día de la semana

Ahora podemos calcular la concentración promedio de NO2 para cada día de la semana en cada ubicación de medición. Esto se puede hacer utilizando el método `groupby`.

```python
# calculate the average NO2 concentration for each day of the week
average_NO2 = air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean()
```

# Agregar una nueva columna para el mes de la medición

Ahora, queremos agregar una nueva columna a nuestro DataFrame que contenga solo el mes de cada medición. Esto se puede lograr utilizando el accesor `dt`.

```python
# add a new column for the month of each measurement
air_quality["month"] = air_quality["datetime"].dt.month
```

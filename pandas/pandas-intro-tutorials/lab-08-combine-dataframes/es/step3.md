# Concatenando los conjuntos de datos

A continuación, combinaremos las mediciones de nitrato y materia particulada en una sola tabla utilizando la función `concat`.

```python
# Concatenate the two dataframes
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
```

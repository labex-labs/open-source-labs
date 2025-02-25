# Convertir cadenas en objetos datetime

Las fechas en la columna "datetime" actualmente son cadenas. Queremos convertirlas en objetos datetime para manipularlas más fácilmente.

```python
# convert "datetime" column to datetime objects
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
```

# Converter strings em objetos datetime

As datas na coluna "datetime" são atualmente strings. Queremos convertê-las em objetos datetime para facilitar a manipulação.

```python
# convert "datetime" column to datetime objects
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
```

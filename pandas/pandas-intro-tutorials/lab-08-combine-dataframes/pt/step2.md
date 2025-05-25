# Carregar os Conjuntos de Dados

Carregaremos dois conjuntos de dados relacionados à qualidade do ar. Um contém dados de Nitrato e o outro contém dados de Material Particulado.

```python
# Load the Nitrate data
air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv", parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]

# Load the Particulate matter data
air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv", parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]
```

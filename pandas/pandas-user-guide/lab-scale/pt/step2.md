# Carregar Menos Dados

Em vez de carregar todos os dados, podemos carregar apenas as colunas que precisamos. Aqui, demonstramos dois métodos para carregar menos dados do arquivo parquet.

```python
# Option 1: Load all data then filter
columns = ["id_0", "name_0", "x_0", "y_0"]
pd.read_parquet("timeseries_wide.parquet")[columns]

# Option 2: Load only the requested columns
pd.read_parquet("timeseries_wide.parquet", columns=columns)
```

# Usar Tipos de Dados Eficientes

Os tipos de dados padrão do Pandas não são os mais eficientes em termos de memória. Este passo mostra como usar tipos de dados mais eficientes para armazenar conjuntos de dados maiores na memória.

```python
ts = make_timeseries(freq="30S", seed=0)
ts.to_parquet("timeseries.parquet")
ts = pd.read_parquet("timeseries.parquet")

# Convert 'name' column to 'category' type for efficiency
ts2 = ts.copy()
ts2["name"] = ts2["name"].astype("category")

# Downcast numeric columns to their smallest types
ts2["id"] = pd.to_numeric(ts2["id"], downcast="unsigned")
ts2[["x", "y"]] = ts2[["x", "y"]].apply(pd.to_numeric, downcast="float")
```

# Использование эффективных типов данных

По умолчанию pandas использует типы данных, которые не всегда являются наиболее экономными по памяти. В этом шаге показано, как использовать более эффективные типы данных для хранения больших наборов данных в памяти.

```python
ts = make_timeseries(freq="30S", seed=0)
ts.to_parquet("timeseries.parquet")
ts = pd.read_parquet("timeseries.parquet")

# Преобразование столбца 'name' в тип 'category' для повышения эффективности
ts2 = ts.copy()
ts2["name"] = ts2["name"].astype("category")

# Сокращение числовых столбцов до наименьших типов
ts2["id"] = pd.to_numeric(ts2["id"], downcast="unsigned")
ts2[["x", "y"]] = ts2[["x", "y"]].apply(pd.to_numeric, downcast="float")
```

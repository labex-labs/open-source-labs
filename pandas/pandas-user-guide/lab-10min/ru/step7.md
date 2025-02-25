# Работа с пропущенными данными

Pandas предоставляет методы для работы с пропущенными данными в DataFrame.

```python
# Filling missing data
df.fillna(value=5)

# Getting the boolean mask where values are nan
pd.isna(df)
```

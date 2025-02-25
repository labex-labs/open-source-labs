# Обнаружение пропущенных значений

Далее мы будем использовать функции `isna` и `notna` для обнаружения пропущенных значений.

```python
# Use isna and notna to detect missing values
pd.isna(df2["one"])
df2["four"].notna()
df2.isna()
```

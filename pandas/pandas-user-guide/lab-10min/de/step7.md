# Umgang mit fehlenden Daten

Pandas bietet Methoden, um fehlende Daten im Dataframe zu behandeln.

```python
# Filling missing data
df.fillna(value=5)

# Getting the boolean mask where values are nan
pd.isna(df)
```

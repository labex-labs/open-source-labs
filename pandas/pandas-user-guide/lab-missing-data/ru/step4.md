# Выполняем вычисления с пропущенными данными

Мы выполним некоторые базовые арифметические и статистические вычисления с пропущенными данными.

```python
# Perform calculations with missing data
df["one"].sum()
df.mean(axis=1, numeric_only=True)
df.cumsum()
```

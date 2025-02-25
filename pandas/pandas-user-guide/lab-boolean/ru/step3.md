# Логические операции Клини

Pandas реализует логику Клини (тризначную логику) для логических операций, таких как `&` (и), `|` (или) и `^` (исключающее или). Это отличается от того, как `np.nan` ведет себя в логических операциях.

```python
# Demonstrating the difference in 'or' operations between np.nan and NA
pd.Series([True, False, np.nan], dtype="object") | True # np.nan behaves differently
pd.Series([True, False, pd.NA], dtype="boolean") | True # NA follows Kleene logic

# Demonstrating the difference in 'and' operations between np.nan and NA
pd.Series([True, False, np.nan], dtype="object") & True # np.nan behaves differently
pd.Series([True, False, pd.NA], dtype="boolean") & True # NA follows Kleene logic
```

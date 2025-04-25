# 克林逻辑运算

Pandas 对逻辑运算（如 `&`（与）、`|`（或）和 `^`（异或））实现了克林逻辑（三值逻辑）。这与 `np.nan` 在逻辑运算中的行为不同。

```python
# 展示 np.nan 和 NA 在“或”运算中的差异
pd.Series([True, False, np.nan], dtype="object") | True # np.nan 行为不同
pd.Series([True, False, pd.NA], dtype="boolean") | True # NA 遵循克林逻辑

# 展示 np.nan 和 NA 在“与”运算中的差异
pd.Series([True, False, np.nan], dtype="object") & True # np.nan 行为不同
pd.Series([True, False, pd.NA], dtype="boolean") & True # NA 遵循克林逻辑
```

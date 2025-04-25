# クリーネの論理演算

Pandas は、`&`（論理積）、`|`（論理和）、`^`（排他的論理和）のような論理演算に対してクリーネ論理（三値論理）を実装しています。これは、論理演算における`np.nan`の振る舞いとは異なります。

```python
# Demonstrating the difference in 'or' operations between np.nan and NA
pd.Series([True, False, np.nan], dtype="object") | True # np.nan behaves differently
pd.Series([True, False, pd.NA], dtype="boolean") | True # NA follows Kleene logic

# Demonstrating the difference in 'and' operations between np.nan and NA
pd.Series([True, False, np.nan], dtype="object") & True # np.nan behaves differently
pd.Series([True, False, pd.NA], dtype="boolean") & True # NA follows Kleene logic
```

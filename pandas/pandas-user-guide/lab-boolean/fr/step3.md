# Opérations logiques de Kleene

Pandas implémente la logique de Kleene (logique trivalente) pour les opérations logiques telles que `&` (et), `|` (ou) et `^` (ou exclusif). Cela diffère de la manière dont `np.nan` se comporte dans les opérations logiques.

```python
# Montre la différence dans les opérations 'ou' entre np.nan et NA
pd.Series([True, False, np.nan], dtype="object") | True # np.nan se comporte différemment
pd.Series([True, False, pd.NA], dtype="boolean") | True # NA suit la logique de Kleene

# Montre la différence dans les opérations 'et' entre np.nan et NA
pd.Series([True, False, np.nan], dtype="object") & True # np.nan se comporte différemment
pd.Series([True, False, pd.NA], dtype="boolean") & True # NA suit la logique de Kleene
```

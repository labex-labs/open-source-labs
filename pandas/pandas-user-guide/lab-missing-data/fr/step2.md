# Découvrir les valeurs manquantes

Ensuite, nous utiliserons les fonctions `isna` et `notna` pour détecter les valeurs manquantes.

```python
# Utilisez isna et notna pour détecter les valeurs manquantes
pd.isna(df2["one"])
df2["four"].notna()
df2.isna()
```

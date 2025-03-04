# Effectuer des calculs avec des données manquantes

Nous allons effectuer quelques calculs arithmétiques et statistiques de base avec des données manquantes.

```python
# Effectuer des calculs avec des données manquantes
df["one"].sum()
df.mean(axis=1, numeric_only=True)
df.cumsum()
```

# Gestion des données manquantes

Pandas fournit des méthodes pour gérer les données manquantes dans le DataFrame.

```python
# Remplissage des données manquantes
df.fillna(value=5)

# Obtenir le masque booléen où les valeurs sont nan
pd.isna(df)
```
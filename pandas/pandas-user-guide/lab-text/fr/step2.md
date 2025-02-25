# Utiliser les méthodes de chaîne de caractères

Pandas fournit une série de méthodes de traitement de chaînes de caractères qui facilitent la manipulation des données de type chaîne. Ces méthodes excluent automatiquement les valeurs manquantes/NA.

```python
s = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
)

# convertir en minuscules
s.str.lower()

# convertir en majuscules
s.str.upper()

# calculer la longueur de chaque chaîne
s.str.len()
```

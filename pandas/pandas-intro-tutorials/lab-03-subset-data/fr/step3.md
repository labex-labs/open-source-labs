# Sélection de plusieurs colonnes

Pour sélectionner plusieurs colonnes, utilisez une liste de noms de colonnes à l'intérieur des crochets de sélection `[]`.

```python
# Sélectionne les colonnes 'Age' et 'Sex'
age_sex = titanic[["Age", "Sex"]]

# Affiche les 5 premières lignes
age_sex.head()
```

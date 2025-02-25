# Indexation avec des valeurs NA

Pandas permet d'effectuer une indexation avec des valeurs `NA` dans un tableau booléen, qui sont considérées comme `False`.

```python
# Création d'une série pandas
s = pd.Series([1, 2, 3])

# Création d'un tableau booléen avec des valeurs NA
mask = pd.array([True, False, pd.NA], dtype="boolean")

# Indexation de la série avec le tableau booléen
s[mask] # Les valeurs NA sont considérées comme False
```

Si vous souhaitez conserver les valeurs `NA`, vous pouvez les remplir manuellement avec `fillna(True)`.

```python
# Remplissage des valeurs NA avec True et indexation de la série
s[mask.fillna(True)]
```

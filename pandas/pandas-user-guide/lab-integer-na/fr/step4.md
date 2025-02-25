# Gérer les valeurs manquantes avec `pandas.NA`

La classe `IntegerArray` utilise `pandas.NA` comme valeur manquante scalaire. Lorsque vous découpez un seul élément manquant, cela renverra `pandas.NA`.

```python
# Créez un `IntegerArray` avec une valeur manquante
a = pd.array([1, None], dtype="Int64")

# Découpez le deuxième élément qui est une valeur manquante
valeur_manquante = a[1]
# Sortie : <NA>
```

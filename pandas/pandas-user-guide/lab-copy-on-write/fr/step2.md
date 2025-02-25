# Comprendre le Copy-On-Write avec DataFrame

Maintenant, créons un DataFrame et voyons comment le Copy-On-Write affecte la modification des données.

```python
# Créer un DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Créer un sous-ensemble du DataFrame
subset = df["foo"]

# Modifier le sous-ensemble
subset.iloc[0] = 100

# Afficher le DataFrame original
print(df)
```

## Implémenter le Copy-On-Write avec DataFrame

Maintenant, voyons comment implémenter le Copy-On-Write lors de la modification d'un DataFrame.

```python
# Activer le Copy-On-Write
pd.options.mode.copy_on_write = True

# Créer un sous-ensemble du DataFrame
subset = df["foo"]

# Modifier le sous-ensemble
subset.iloc[0] = 100

# Afficher le DataFrame original
print(df)
```

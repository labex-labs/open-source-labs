# Trouvez le nom le plus long

Découvrez quel passager du Titanic a le nom le plus long. Nous utiliserons la méthode `str.len()` pour obtenir la longueur de chaque nom, et la méthode `idxmax()` pour trouver l'index du nom le plus long.

```python
# Obtenez la longueur de chaque nom
name_lengths = titanic["Name"].str.len()

# Trouvez l'index du nom le plus long
longest_name_index = name_lengths.idxmax()

# Obtenez le nom le plus long
longest_name = titanic.loc[longest_name_index, "Name"]
```

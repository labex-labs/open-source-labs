# Implémenter l'affectation en chaîne avec Copy-On-Write

Enfin, voyons comment implémenter l'affectation en chaîne avec Copy-On-Write en utilisant la méthode `loc`.

```python
# Créer un DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Appliquer une affectation en chaîne avec Copy-On-Write en utilisant 'loc'
df.loc[df["bar"] > 5, "foo"] = 100

# Afficher le DataFrame
print(df)
```

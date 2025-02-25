# Comprendre l'affectation en chaîne avec Copy-On-Write

Maintenant, comprenons comment l'affectation en chaîne fonctionne avec Copy-On-Write.

```python
# Créer un DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Appliquer une affectation en chaîne, qui violerait les principes de Copy-On-Write
df["foo"][df["bar"] > 5] = 100

# Afficher le DataFrame
print(df)
```

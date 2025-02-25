# Mutation avec des méthodes de Fonction Utilisateur Définie (UDF)

Lorsque vous utilisez une méthode pandas qui prend une UDF, évitez de modifier le DataFrame à l'intérieur de la UDF. Au lieu de cela, faites une copie avant de faire des modifications.

```python
def f(s):
    s = s.copy()
    s.pop("a")
    return s

df = pd.DataFrame({"a": [1, 2, 3], 'b': [4, 5, 6]})
df.apply(f, axis="columns")
```

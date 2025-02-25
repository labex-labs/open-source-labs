# Créer des variables indicatrices

Vous pouvez créer des variables indicatrices à partir de données de chaîne de caractères en utilisant la méthode `get_dummies`.

```python
# créer des variables indicatrices
s = pd.Series(["a", "a|b", np.nan, "a|c"], dtype="string")
s.str.get_dummies(sep="|")
```

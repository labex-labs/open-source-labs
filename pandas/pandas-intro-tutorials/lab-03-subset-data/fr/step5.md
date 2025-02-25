# Sélectionner des lignes et des colonnes spécifiques

Pour sélectionner à la fois des lignes et des colonnes d'un coup, nous utilisons les opérateurs `loc` ou `iloc`.

```python
# Sélectionne le 'Name' des passagers âgés de plus de 35 ans
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

# Affiche les 5 premières lignes
adult_names.head()
```

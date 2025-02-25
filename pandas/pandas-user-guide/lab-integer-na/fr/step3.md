# Effectuer des opérations avec des tableaux d'entiers pouvant contenir des valeurs manquantes

Vous pouvez effectuer diverses opérations avec des tableaux d'entiers pouvant contenir des valeurs manquantes, telles que des opérations arithmétiques, des comparaisons et des découpes.

```python
# Créez une `Series` avec un type d'entier pouvant contenir des valeurs manquantes
s = pd.Series([1, 2, None], dtype="Int64")

# Effectuez une opération arithmétique
s_plus_un = s + 1 # ajoute 1 à chaque élément de la `Series`

# Effectuez une comparaison
comparaison = s == 1 # vérifie si chaque élément de la `Series` est égal à 1

# Effectuez une opération de découpe
decoupe = s.iloc[1:3] # sélectionne le deuxième et le troisième élément de la `Series`
```

# Défi : Conversion d'un entier en nombre romain

## Problème

Écrivez une fonction `to_roman_numeral(num)` qui prend un entier `num` compris entre 1 et 3999 (inclus) et renvoie sa représentation en nombre romain sous forme de chaîne de caractères.

Pour convertir un entier en sa représentation en nombre romain, vous pouvez utiliser une liste de correspondance contenant des tuples de la forme (valeur romaine, entier). Vous pouvez ensuite utiliser une boucle `for` pour itérer sur les valeurs de la liste de correspondance et utiliser `divmod()` pour mettre à jour `num` avec le reste, ajoutant la représentation en nombre romain au résultat.

Votre fonction devrait renvoyer la représentation en nombre romain de l'entier d'entrée.

## Exemple

```python
to_roman_numeral(3) # 'III'
to_roman_numeral(11) # 'XI'
to_roman_numeral(1998) # 'MCMXCVIII'
```

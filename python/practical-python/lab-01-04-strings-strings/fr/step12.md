# Exercice 1.13 : Extraction de caractères individuels et de sous-chaînes

Les chaînes de caractères sont des tableaux de caractères. Essayez d'extraire quelques caractères :

```python
>>> symbols[0]
?
>>> symbols[1]
?
>>> symbols[2]
?
>>> symbols[-1]        # Dernier caractère
?
>>> symbols[-2]        # Les indices négatifs sont à partir de la fin de la chaîne
?
>>>
```

En Python, les chaînes de caractères sont en lecture seule.

Vérifiez-le en essayant de changer le premier caractère de `symbols` en 'a' en minuscules.

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

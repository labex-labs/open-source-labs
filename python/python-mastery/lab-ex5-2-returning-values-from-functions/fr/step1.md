# Retourner plusieurs valeurs

Supposons que vous écriviez du code pour analyser des fichiers de configuration composés de lignes comme celle-ci :

    nom=valeur

Écrivez une fonction `parse_line(ligne)` qui prend une telle ligne et renvoie à la fois le nom associé et la valeur. La convention commune pour renvoyer plusieurs valeurs est de les renvoyer dans un tuple. Par exemple :

```python
>>> parse_line('email=guido@python.org')
('email', 'guido@python.org')
>>> nom, val = parse_line('email=guido@python.org')
>>> nom
'email'
>>> val
'guido@python.org'
>>>
```

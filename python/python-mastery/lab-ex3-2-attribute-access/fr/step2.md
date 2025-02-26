# Utilisation de getattr()

La fonction `getattr()` est très utile pour écrire du code qui traite les objets de manière extrêmement générique. Pour illustrer, considérez cet exemple qui affiche un ensemble d'attributs définis par l'utilisateur :

```python
>>> s= Stock('GOOG', 100, 490.1)
>>> fields = ['name','shares','price']
>>> for name in fields:
           print(name, getattr(s, name))

name GOOG
shares 100
price 490.1
>>>
```

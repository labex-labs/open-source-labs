# Copies profondes

Parfois, vous avez besoin de créer une copie d'un objet et de tous les objets qu'il contient. Vous pouvez utiliser le module `copy` pour ce faire :

```python
>>> a = [2,3,[100,101],4]
>>> import copy
>>> b = copy.deepcopy(a)
>>> a[2].append(102)
>>> b[2]
[100,101]
>>> a[2] is b[2]
False
>>>
```

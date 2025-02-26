# Copias profundas

A veces es necesario hacer una copia de un objeto y de todos los objetos que contiene. Puedes utilizar el módulo `copy` para esto:

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

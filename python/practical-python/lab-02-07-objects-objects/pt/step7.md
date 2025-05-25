# Cópias profundas (Deep copies)

Às vezes, você precisa fazer uma cópia de um objeto e de todos os objetos contidos nele. Você pode usar o módulo `copy` para isso:

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

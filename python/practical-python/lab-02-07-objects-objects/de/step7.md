# Tiefkopien

Manchmal müssen Sie eine Kopie eines Objekts und aller darin enthaltenen Objekte erstellen. Hierfür können Sie das `copy`-Modul verwenden:

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

# Deep copies

Sometimes you need to make a copy of an object and all the objects contained within it.
You can use the `copy` module for this:

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

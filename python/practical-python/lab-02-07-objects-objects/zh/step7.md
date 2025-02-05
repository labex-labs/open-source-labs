# 深拷贝

有时你需要复制一个对象以及它所包含的所有对象。你可以使用 `copy` 模块来实现这一点：

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

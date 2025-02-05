# 元素访问的特殊方法

这些是用于实现容器的方法。

```python
len(x)      x.__len__()
x[a]        x.__getitem__(a)
x[a] = v    x.__setitem__(a,v)
del x[a]    x.__delitem__(a)
```

你可以在你的类中使用它们。

```python
class Sequence:
    def __len__(self):
     ...
    def __getitem__(self,a):
     ...
    def __setitem__(self,a,v):
     ...
    def __delitem__(self,a):
     ...
```

# Métodos especiales para el acceso a elementos

Estos son los métodos para implementar contenedores.

```python
len(x)      x.__len__()
x[a]        x.__getitem__(a)
x[a] = v    x.__setitem__(a,v)
del x[a]    x.__delitem__(a)
```

Puedes utilizarlos en tus clases.

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

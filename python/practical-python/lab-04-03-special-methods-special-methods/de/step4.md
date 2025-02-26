# Spezielle Methoden für den Zugriff auf Elemente

Dies sind die Methoden, um Container zu implementieren.

```python
len(x)      x.__len__()
x[a]        x.__getitem__(a)
x[a] = v    x.__setitem__(a,v)
del x[a]    x.__delitem__(a)
```

Sie können sie in Ihren Klassen verwenden.

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

# Méthodes spéciales pour l'accès aux éléments

Ce sont les méthodes pour implémenter des conteneurs.

```python
len(x)      x.__len__()
x[a]        x.__getitem__(a)
x[a] = v    x.__setitem__(a,v)
del x[a]    x.__delitem__(a)
```

Vous pouvez les utiliser dans vos classes.

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

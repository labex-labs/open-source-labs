# Réaffectation des segments

Sur les listes, les segments peuvent être réaffectés et supprimés.

```python
# Réaffectation
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12]       # [0,1,10,11,12,4,5,6,7,8]
```

_Nota : Le segment réaffecté n'a pas besoin d'avoir la même longueur._

```python
# Suppression
a = [0,1,2,3,4,5,6,7,8]
del a[2:4]                # [0,1,4,5,6,7,8]
```

# Slice-Zuweisung neu

Bei Listen können Slices neu zugewiesen und gelöscht werden.

```python
# Neuzuweisung
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12]       # [0,1,10,11,12,4,5,6,7,8]
```

_Hinweis: Der neu zugewiesene Slice muss nicht die gleiche Länge haben._

```python
# Löschung
a = [0,1,2,3,4,5,6,7,8]
del a[2:4]                # [0,1,4,5,6,7,8]
```

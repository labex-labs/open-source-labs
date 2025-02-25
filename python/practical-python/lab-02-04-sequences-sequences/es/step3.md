# Reasignación de rebanadas

En las listas, las rebanadas se pueden reasignar y eliminar.

```python
# Reasignación
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12]       # [0,1,10,11,12,4,5,6,7,8]
```

_Nota: La rebanada reasignada no necesita tener la misma longitud._

```python
# Eliminación
a = [0,1,2,3,4,5,6,7,8]
del a[2:4]                # [0,1,4,5,6,7,8]
```

# Reatribuição de Fatias (Slice re-assignment)

Em listas, fatias (slices) podem ser reatribuídas e excluídas.

```python
# Reatribuição (Reassignment)
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12]       # [0,1,10,11,12,4,5,6,7,8]
```

_Nota: A fatia reatribuída não precisa ter o mesmo comprimento._

```python
# Exclusão (Deletion)
a = [0,1,2,3,4,5,6,7,8]
del a[2:4]                # [0,1,4,5,6,7,8]
```

# Slice re-assignment

On lists, slices can be reassigned and deleted.

```python
# Reassignment
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12]       # [0,1,10,11,12,4,5,6,7,8]
```

_Note: The reassigned slice doesn't need to have the same length._

```python
# Deletion
a = [0,1,2,3,4,5,6,7,8]
del a[2:4]                # [0,1,4,5,6,7,8]
```

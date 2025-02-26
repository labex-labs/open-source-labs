# Reasignación de valores

Reasignar un valor _nunca_ sobrescribe la memoria utilizada por el valor anterior.

```python
a = [1,2,3]
b = a
a = [4,5,6]

print(a)      # [4, 5, 6]
print(b)      # [1, 2, 3]    Conserva el valor original
```

Recuerde: **Las variables son nombres, no ubicaciones de memoria.**

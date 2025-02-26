# Réaffectation de valeurs

La réaffectation d'une valeur _n'écrase jamais_ la mémoire utilisée par la valeur précédente.

```python
a = [1,2,3]
b = a
a = [4,5,6]

print(a)      # [4, 5, 6]
print(b)      # [1, 2, 3]    Conserve la valeur d'origine
```

Rappelez-vous : **Les variables sont des noms, pas des emplacements mémoire.**

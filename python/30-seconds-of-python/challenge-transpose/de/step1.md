# Matrix transponieren

## Problemstellung

Schreiben Sie eine Funktion namens `transpose(lst)`, die eine zweidimensionale Liste als Argument nimmt und die Transponierte der angegebenen Liste zurückgibt.

Verfolgen Sie diese Schritte, um das Problem zu lösen:

- Verwenden Sie `*lst`, um die bereitgestellte Liste als Tupel zu erhalten.
- Verwenden Sie `zip()` in Kombination mit `list()`, um die Transponierte der angegebenen zweidimensionalen Liste zu erstellen.

## Beispiel

```python
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
```

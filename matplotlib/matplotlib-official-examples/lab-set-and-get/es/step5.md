# Alias

Para reducir las pulsaciones de teclado en modo interactivo, un número de propiedades tienen alias cortos, por ejemplo, 'lw' para 'linewidth' y'mec' para'markeredgecolor'. Cuando se llama a set o get en modo de introspección, estas propiedades se listarán como 'fullname' o 'aliasname'.

```python
l1, l2 = plt.plot([1, 2, 3], [2, 3, 4], [1, 2, 3], [3, 4, 5])
plt.setp(l1, linewidth=2, color='r')
plt.setp(l2, linewidth=1, color='g')
```

# Alias

Pour réduire le nombre de frappes en mode interactif, un certain nombre de propriétés ont des alias courts, par exemple, 'lw' pour 'linewidth' et'mec' pour'markeredgecolor'. Lors de l'appel de set ou get en mode d'introspection, ces propriétés seront listées comme 'fullname' ou 'aliasname'.

```python
l1, l2 = plt.plot([1, 2, 3], [2, 3, 4], [1, 2, 3], [3, 4, 5])
plt.setp(l1, linewidth=2, color='r')
plt.setp(l2, linewidth=1, color='g')
```

# Aliases (Alias)

Para reduzir as batidas de teclado no modo interativo, um número de propriedades tem aliases (alias) curtos, por exemplo, 'lw' para 'linewidth' e 'mec' para 'markeredgecolor'. Ao chamar set ou get no modo de introspecção, essas propriedades serão listadas como 'fullname' ou 'aliasname'.

```python
l1, l2 = plt.plot([1, 2, 3], [2, 3, 4], [1, 2, 3], [3, 4, 5])
plt.setp(l1, linewidth=2, color='r')
plt.setp(l2, linewidth=1, color='g')
```

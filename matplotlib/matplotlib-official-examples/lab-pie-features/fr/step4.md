# Ajouter des étiquettes aux tranches

Nous pouvons ajouter des étiquettes aux tranches en passant une liste d'étiquettes au paramètre `labels` de la fonction `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
```

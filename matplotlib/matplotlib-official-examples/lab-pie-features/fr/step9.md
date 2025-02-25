# Modifier l'ombre

Nous pouvons modifier l'ombre du diagramme circulaire à secteurs en passant un dictionnaire d'arguments au paramètre `shadow` de la fonction `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow={'ox': -0.04, 'edgecolor': 'none','shade': 0.9}, startangle=90)
```

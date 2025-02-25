# Éclater les tranches

Nous pouvons éclater une ou plusieurs tranches du diagramme circulaire à secteurs en passant une liste de valeurs au paramètre `explode` de la fonction `pie()`.

```python
explode = (0, 0.1, 0, 0)  # seulement "éclater" la 2e tranche (c'est-à-dire 'Porcs')

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
```

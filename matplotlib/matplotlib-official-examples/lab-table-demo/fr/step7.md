# Ajouter un tableau au graphique

Nous allons ajouter un tableau en bas du graphique en utilisant la fonction `plt.table`. Nous passerons le texte des cellules, les étiquettes de ligne, les couleurs de ligne et les étiquettes de colonne en tant que paramètres à la fonction.

```python
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
```

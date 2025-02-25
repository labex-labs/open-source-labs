# Création d'un graphique en barres empilées verticales

Nous allons créer un graphique en barres empilées verticales en utilisant la fonction `plt.bar` pour représenter les pertes subies par différents désastres naturels au fil des ans. Nous utiliserons une boucle `for` pour itérer sur chaque ligne de données et tracer les barres.

```python
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

y_offset = np.zeros(len(columns))

cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
```

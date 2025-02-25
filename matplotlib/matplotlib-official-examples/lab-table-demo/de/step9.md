# Achsenbeschriftungen und Titel hinzufügen

Wir werden Achsenbeschriftungen und einen Titel zum Diagramm hinzufügen, indem wir die Funktionen `plt.ylabel`, `plt.yticks`, `plt.xticks` und `plt.title` verwenden.

```python
values = np.arange(0, 2500, 500)
value_increment = 1000

plt.ylabel(f"Verlust in ${value_increment}'s")
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Verlust durch Katastrophe')
```

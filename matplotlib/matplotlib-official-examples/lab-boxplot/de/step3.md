# Standard-Boxplot

Wir beginnen mit der Erstellung eines Standard-Boxplots, um die Daten zu visualisieren. Wir werden die Matplotlib-Funktion `boxplot()` verwenden und die Daten und Bezeichnungen als Argumente übergeben. Wir setzen auch den Titel des Diagramms mit der Funktion `set_title()`.

```python
fig, ax = plt.subplots()
ax.boxplot(data, labels=labels)
ax.set_title('Default Box Plot')
plt.show()
```

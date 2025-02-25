# Tabelle zum Diagramm hinzufügen

Wir werden eine Tabelle am unteren Rand des Diagramms mit der `plt.table`-Funktion hinzufügen. Wir werden die Zelltexte, Zeilenbezeichnungen, Zeilenfarben und Spaltenbezeichnungen als Parameter an die Funktion übergeben.

```python
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
```

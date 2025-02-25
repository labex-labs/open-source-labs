# Anpassen des Diagramms

Wir können das Diagramm anpassen, indem wir Beschriftungen, einen Titel hinzufügen und die Beschriftungen der x-Achsenmarkierungen und die Legende anpassen. Wir werden auch die y-Achsengrenze festlegen, um sicherzustellen, dass all unsere Daten sichtbar sind.

```python
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)
```

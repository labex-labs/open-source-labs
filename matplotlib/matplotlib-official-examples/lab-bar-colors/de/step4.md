# Das Diagramm anpassen

Wir können das Diagramm weiter anpassen, indem wir Achsenbeschriftungen und einen Titel hinzufügen. Wir können auch die Farbe der Achsenbeschriftungen und des Legendentitels ändern. Der folgende Code zeigt, wie das Diagramm angepasst wird:

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply', color='blue')
ax.set_xlabel('fruit names', color='blue')
ax.set_title('Fruit supply by kind and color', color='purple')
ax.legend(title='Fruit color', title_color='red', labelcolor='green')
plt.show()
```

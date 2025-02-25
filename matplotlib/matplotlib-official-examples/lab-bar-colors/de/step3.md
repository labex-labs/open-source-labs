# Den Balkendiagramm erstellen

Jetzt können wir das Balkendiagramm mit den Daten erstellen, die wir in Schritt 2 definiert haben. Wir werden die `bar()`-Methode des `pyplot`-Moduls von Matplotlib verwenden, um das Diagramm zu erstellen. Wir werden auch die Parameter `label` und `color` übergeben, um die Legendentexte und die Balkenfarben respective zu steuern. Der folgende Code zeigt, wie das Balkendiagramm erstellt wird:

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')
plt.show()
```

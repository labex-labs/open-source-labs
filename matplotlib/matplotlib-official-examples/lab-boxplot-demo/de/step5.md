# Hinzufügen von Beschriftungen und Titeln

Schließlich können wir unserem Boxplot Beschriftungen und Titel hinzufügen, um es informativer zu gestalten. Wir können Beschriftungen für die x- und y-Achsen sowie einen Titel für das Diagramm hinzufügen. Wir können auch die Schriftgröße und den Stil der Beschriftungen und des Titels ändern. Hier ist ein Beispiel dafür, wie man Beschriftungen und Titel hinzufügt:

```python
plt.boxplot([data1, data2, data3])
plt.xlabel('Group')
plt.ylabel('Value')
plt.title('Comparison of Three Groups')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
```

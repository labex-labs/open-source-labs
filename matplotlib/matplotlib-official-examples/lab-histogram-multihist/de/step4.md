# Fügen Sie Beschriftungen und einen Titel hinzu

Wir können Beschriftungen für die x- und y-Achsen und einen Titel für das Diagramm hinzufügen, indem wir die Funktionen `xlabel`, `ylabel` und `title` verwenden.

```python
plt.hist(x, n_bins)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()
```

# Speichern des Diagramms

Sobald wir ein Diagramm erstellt haben, können wir es in einer Datei speichern.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.savefig('my_plot.png')
```

Hier verwenden wir die `savefig`-Funktion, um unser Diagramm in einer Datei namens `my_plot.png` zu speichern.

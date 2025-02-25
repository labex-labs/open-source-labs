# Erstellen eines Balkendiagramms

In diesem Schritt werden wir ein Balkendiagramm mit Matplotlib erstellen. Wir beginnen damit, einige Daten zu generieren, die wir mit der NumPy-Funktion `random()` plotten werden. Anschließend werden wir die `bar()`-Funktion verwenden, um das Diagramm zu erstellen.

```python
x = ['A', 'B', 'C', 'D', 'E']
y = np.random.randint(1, 10, 5)

plt.bar(x, y)
plt.show()
```

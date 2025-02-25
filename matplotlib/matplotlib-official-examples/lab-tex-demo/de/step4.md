# Erstellen eines Streudiagramms

In diesem Schritt werden wir ein Streudiagramm mit Matplotlib erstellen. Wir beginnen damit, einige zufällige Daten zu generieren, die wir mit der NumPy-Funktion `random()` plotten werden. Anschließend werden wir die `scatter()`-Funktion verwenden, um das Diagramm zu erstellen.

```python
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y)
plt.show()
```

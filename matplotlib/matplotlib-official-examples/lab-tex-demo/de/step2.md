# Erstellen eines einfachen Linien-Diagramms

In diesem Schritt werden wir ein einfaches Linien-Diagramm mit Matplotlib erstellen. Wir beginnen damit, einige Daten zu generieren, die wir mit der NumPy-Funktion `linspace()` und der `cos()`-Funktion plotten werden. Anschließend werden wir die `plot()`-Funktion verwenden, um das Diagramm zu erstellen.

```python
t = np.linspace(0.0, 1.0, 100)
s = np.cos(4 * np.pi * t) + 2

plt.plot(t, s)
plt.show()
```

# Erstellen eines einfachen Diagramms

Nachdem wir Matplotlib importiert haben, können wir mit der Erstellung von Visualisierungen beginnen. Lassen Sie uns mit der Erstellung eines einfachen Diagramms starten.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.show()
```

Hier erstellen wir zwei Listen `x` und `y`, die die x- und y-Werte für unser Diagramm enthalten. Anschließend verwenden wir die `plot`-Funktion, um ein Liniendiagramm von `x` und `y` zu erstellen. Schließlich verwenden wir die `show`-Funktion, um das Diagramm anzuzeigen.

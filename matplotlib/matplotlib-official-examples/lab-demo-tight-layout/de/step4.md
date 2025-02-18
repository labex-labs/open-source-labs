# Erstellen mehrerer Diagramme

Wir können auch mehrere Diagramme in derselben Abbildung erstellen.

```python
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('Plot 1')

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Plot 2')

plt.show()
```

Hier verwenden wir die `subplot`-Funktion, um zwei Diagramme nebeneinander in derselben Abbildung zu erstellen. Wir übergeben drei Argumente an `subplot`: die Anzahl der Zeilen, die Anzahl der Spalten und die Nummer des Diagramms. Anschließend erstellen wir in jedem Unterdiagramm ein Diagramm.

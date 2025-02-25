# Erstellen des ersten Plots

Lassen Sie uns nun das erste Diagramm mit `subplot` erstellen. `subplot` nimmt drei Argumente: die Anzahl der Zeilen, die Anzahl der Spalten und die Diagrammnummer. In diesem Beispiel werden wir ein Diagramm mit 2 Zeilen und 1 Spalte (`211`) erstellen, was bedeutet, dass das erste Diagramm in der obersten Zeile sein wird.

```python
ax1 = plt.subplot(211)
ax1.plot(t, np.sin(2*np.pi*t))
```

# Generieren von Daten für die Säulendiagramme

Wir werden nun die Daten für die Säulendiagramme generieren. Wir werden vier Datensätze erstellen, jeder mit 20 Werten. Wir werden die NumPy-`arange()`-Methode verwenden, um ein Array von 20 Werten zu erstellen, und die NumPy-`random.rand()`-Methode, um für jeden Datensatz zufällige Werte zu generieren.

```python
colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]
for c, k in zip(colors, yticks):
    xs = np.arange(20)
    ys = np.random.rand(20)
```

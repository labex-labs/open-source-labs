# Daten definieren

Der nächste Schritt besteht darin, die Daten zu definieren, die wir in unserem Graphen verwenden werden. Wir werden die `arange`-Funktion von NumPy verwenden, um ein Array von Werten von 0 bis 5 mit einem Schritt von 0,1 zu erstellen. Dieses Array werden wir als x-Achse verwenden. Wir werden auch die y-Achse definieren, indem wir die Exponentialfunktion und die Sinusfunktion von NumPy verwenden.

```python
# Define the data
t = np.arange(0.0, 5.0, 0.1)
s = np.exp(-t) + np.sin(2 * np.pi * t) + 1
```

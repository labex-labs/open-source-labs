# Visualisierung des Datensatzes

Wir werden nun den Datensatz mit matplotlib visualisieren. Wir werden die Werte von X gegen die Werte von y aufzeichnen.

```python
plt.plot(X, y, "b.")
plt.title("Dataset with Strong Outliers")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```

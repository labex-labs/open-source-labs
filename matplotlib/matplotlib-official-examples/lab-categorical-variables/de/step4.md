# Streudiagramm

Wir können auch ein Streudiagramm erstellen, um die Beziehung zwischen zwei kategorischen Variablen zu zeigen. In diesem Fall werden wir die gleichen Frucht-Daten verwenden und der Anzahl zufälliger Störungen hinzufügen, um eine zweite Variable zu erstellen.

```python
noise = np.random.rand(len(values)) * 5
plt.scatter(names, values + noise)
plt.title('Fruit Counts with Noise')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
```

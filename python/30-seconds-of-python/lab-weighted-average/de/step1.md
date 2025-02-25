# Gewichteter Mittelwert

Schreiben Sie eine Funktion `weighted_average(nums, weights)`, die zwei Listen gleicher Länge annimmt: `nums` und `weights`. Die Funktion sollte den gewichteten Mittelwert der Zahlen in `nums` zurückgeben, wobei jede Zahl mit ihrem entsprechenden Gewicht in `weights` multipliziert wird. Der gewichtete Mittelwert wird berechnet, indem die Summe der Produkte jeder Zahl und ihres Gewichts durch die Summe der Gewichte dividiert wird.

```python
def weighted_average(nums, weights):
  return sum(x * y for x, y in zip(nums, weights)) / sum(weights)
```

```python
weighted_average([1, 2, 3], [0.6, 0.2, 0.3]) # 1.72727
```

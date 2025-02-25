# Beispiel-Datensätze erstellen

Als nächstes werden wir Beispiel-Datensätze erstellen, die wir für unsere Histogramme verwenden. Wir werden drei Datensätze mit jeweils 387 Datenpunkten erstellen:

```python
np.random.seed(19680801)
number_of_data_points = 387
labels = ["A", "B", "C"]
data_sets = [np.random.normal(0, 1, number_of_data_points),
             np.random.normal(6, 1, number_of_data_points),
             np.random.normal(-3, 1, number_of_data_points)]
```

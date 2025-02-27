# Parameter festlegen

Wir müssen die Parameter festlegen, die die Größe der Datensätze, die Anzahl der Iterationen und die Standardabweichung des Rauschens steuern.

```python
n_repeat = 50  # Anzahl der Iterationen zur Berechnung von Erwartungswerten
n_train = 50  # Größe des Trainingssatzes
n_test = 1000  # Größe des Testsatzes
noise = 0.1  # Standardabweichung des Rauschens
np.random.seed(0)
```

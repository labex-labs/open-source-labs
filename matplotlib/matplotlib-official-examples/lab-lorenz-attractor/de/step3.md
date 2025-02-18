# Die Anfangsparameter festlegen

Wir legen die Anfangsparameter für die Simulation fest, einschließlich des Zeitschritts `dt`, der Anzahl der Schritte `num_steps` und der Anfangswerte für `x`, `y` und `z`.

```python
dt = 0.01
num_steps = 10000

xyzs = np.empty((num_steps + 1, 3))  # Need one more for the initial values
xyzs[0] = (0., 1., 1.05)  # Set initial values
```

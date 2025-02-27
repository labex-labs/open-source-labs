# Parameter für den Toy-Datensatz festlegen

In diesem Schritt legen wir die Parameter für den Toy-Datensatz fest, die die Zufallszahl, die Anzahl der Komponenten, die Anzahl der Merkmale, die Farben, die Kovarianzen, die Stichproben und die Mittelwerte umfassen.

```python
random_state, n_components, n_features = 2, 3, 2
colors = np.array(["#0072B2", "#F0E442", "#D55E00"])
covars = np.array(
    [[[0.7, 0.0], [0.0, 0.1]], [[0.5, 0.0], [0.0, 0.1]], [[0.5, 0.0], [0.0, 0.1]]]
)
samples = np.array([200, 500, 200])
means = np.array([[0.0, -0.70], [0.0, 0.0], [0.0, 0.70]])
```

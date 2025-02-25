# Zufällige Daten generieren

In diesem Schritt generierst du zufällige Daten für die Fähigkeit des Wurfers, den Abflugwinkel, die Kraft, den Erfolg und die Position. Insbesondere generierst du 25 Datenpunkte für jede Variable, außer für die Position, die für jeden Datenpunkt 2 Koordinaten haben wird.

```python
N = 25
np.random.seed(42)
skills = np.random.uniform(5, 80, size=N) * 0.1 + 5
takeoff_angles = np.random.normal(0, 90, N)
thrusts = np.random.uniform(size=N)
successful = np.random.randint(0, 3, size=N)
positions = np.random.normal(size=(N, 2)) * 5
data = zip(skills, takeoff_angles, thrusts, successful, positions)
```

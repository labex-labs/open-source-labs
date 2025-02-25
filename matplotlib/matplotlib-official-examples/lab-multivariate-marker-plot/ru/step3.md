# Генерация случайных данных

В этом шаге вы сгенерируете случайные данные для навыка броска, угла взлета, тяги, успеха и позиции. В частности, вы сгенерируете 25 точек данных для каждой переменной, за исключением позиции, которая будет иметь 2 координаты для каждой точки данных.

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

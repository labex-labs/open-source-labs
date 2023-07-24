# Generate Random Data

In this step, you will generate random data for the skill of the thrower, take-off angle, thrust, success, and position. Specifically, you will generate 25 data points for each variable, except for position, which will have 2 coordinates for each data point.

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

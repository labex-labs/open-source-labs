# 生成随机数据

在这一步中，你将为投掷者的技能、起飞角度、推力、是否成功以及位置生成随机数据。具体来说，你将为每个变量生成25个数据点，但位置变量每个数据点有两个坐标。

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

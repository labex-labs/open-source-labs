# 랜덤 데이터 생성

이 단계에서는 투구자의 기술, 이륙 각도, 추력, 성공 여부 및 위치에 대한 랜덤 데이터를 생성합니다. 구체적으로, 각 변수에 대해 25 개의 데이터 포인트를 생성하며, 위치의 경우 각 데이터 포인트마다 2 개의 좌표가 있습니다.

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

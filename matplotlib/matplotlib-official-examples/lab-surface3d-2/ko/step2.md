# 데이터 생성

다음 단계는 3D 표면에 대한 데이터를 생성하는 것입니다. `u`, `v`, `x`, `y`, 및 `z`를 정의해야 합니다. 이 변수들은 표면을 플롯하는 데 필요한 각도와 좌표를 나타냅니다. NumPy 의 `linspace()` 함수는 각도를 생성하는 데 사용되며, `outer()` 함수는 좌표를 생성하는 데 사용됩니다.

```python
# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
```

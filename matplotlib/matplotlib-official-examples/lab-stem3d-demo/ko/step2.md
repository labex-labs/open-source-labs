# 데이터 정의

이 단계에서는 3D 줄기 플롯을 생성하는 데 사용할 데이터를 정의합니다. 각도에 대한 linspace 배열을 생성하고, 사인 및 코사인 함수를 사용하여 x 및 y 좌표를 계산합니다. 또한 z 좌표를 각도로 정의합니다.

```python
theta = np.linspace(0, 2*np.pi)
x = np.cos(theta - np.pi/2)
y = np.sin(theta - np.pi/2)
z = theta
```

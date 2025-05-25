# 데이터 생성

다음으로, 와이어프레임 플롯을 생성하는 데 사용할 데이터를 생성합니다. 이 랩에서는 `np.meshgrid()` 함수를 사용하여 X, Y, Z 좌표를 생성합니다.

```python
# Generate data
X, Y = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.25))
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```

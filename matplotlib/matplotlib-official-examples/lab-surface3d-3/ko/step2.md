# 표면 플롯을 위한 데이터 생성

이 단계에서는 표면 플롯을 위한 데이터를 생성합니다. X 및 Y 값의 메쉬 그리드 (meshgrid) 를 생성하고, 반경 거리 R 을 계산하며, `np.sin()`을 사용하여 R 값을 기반으로 Z 값을 계산합니다.

```python
# Create data for the surface plot
X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```

# 데이터 생성

Numpy 라이브러리를 사용하여 streamplot 에 대한 데이터를 생성합니다. 이 예제에서는 양방향으로 100 개의 점을 가진 meshgrid 를 생성하고 벡터 필드의 U 및 V 구성 요소를 계산합니다.

```python
w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)
```

# 플롯을 위한 데이터 생성

NumPy 를 사용하여 플롯할 데이터를 생성합니다. -pi/2와 pi/2 사이의 31 개의 데이터 포인트를 생성하고, 이 값들의 코사인을 3 제곱하여 계산합니다.

```python
x = np.linspace(-np.pi/2, np.pi/2, 31)
y = np.cos(x)**3
```

# 데이터 생성

```python
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```

플롯에 사용할 데이터를 생성합니다. -5 에서 5 까지 0.25 간격으로 균등하게 간격을 둔 값으로 배열로 `X` 및 `Y` 값을 생성합니다. 그런 다음 `np.meshgrid()`를 사용하여 `X` 및 `Y` 값의 meshgrid 를 생성합니다. meshgrid 를 사용하여 원점으로부터의 거리인 `R` 값을 계산합니다. 그런 다음 `R`의 `sin()` 함수를 사용하여 `Z` 값을 계산합니다.

# 시각화를 위한 데이터 생성

다음으로, 시각화에 사용할 2D 그리드를 생성합니다. NumPy 의 `meshgrid` 함수를 사용하여 그리드를 생성할 수 있습니다. `meshgrid` 함수는 그리드 점의 좌표를 나타내는 두 개의 벡터 `x`와 `y`가 주어지면 점의 그리드를 생성합니다. 다음 코드 블록을 사용하여 5x5 점의 그리드를 생성합니다.

```python
nrows = 5
ncols = 5
x = np.arange(ncols + 1)
y = np.arange(nrows + 1)
X, Y = np.meshgrid(x, y)
Z = X + Y
```
